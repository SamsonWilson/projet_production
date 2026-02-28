import json

from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

from produition.models import Message


class MessagesView(LoginRequiredMixin, ListView):
    """Vue principale – liste tous les messages par statut."""
    model = Message
    template_name = "Admin/Page_Backend/message.html"
    context_object_name = "all_messages"
    login_url = 'connexion'

    def get_queryset(self):
        return Message.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages_nouveaux'] = Message.objects.filter(
            status='nouveau').order_by('-created_at')
        context['messages_lus'] = Message.objects.filter(
            status__in=['lu', 'repondu']).order_by('-created_at')
        context['messages_archives'] = Message.objects.filter(
            status='archive').order_by('-created_at')
        context['count_nouveau'] = Message.objects.filter(status='nouveau').count()
        context['count_lu'] = Message.objects.filter(
            status__in=['lu', 'repondu']).count()
        context['count_archive'] = Message.objects.filter(status='archive').count()
        context['count_total'] = Message.objects.count()
        return context


# ── AJAX helpers ──────────────────────────────────────────────────────────────

class MessageMarkReadView(View):
    """POST /messages/<pk>/read/  → marque comme lu et retourne les données JSON."""

    def post(self, request, pk):
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'error', 'message': 'Non authentifié'}, status=401)
        message = get_object_or_404(Message, pk=pk)
        message.mark_as_read()
        return JsonResponse({
            'status': 'success',
            'data': {
                'id': message.pk,
                'sender_name': message.sender_name,
                'sender_email': message.sender_email,
                'sender_phone': message.sender_phone or '',
                'subject': message.subject,
                'message': message.message,
                'category': message.category,
                'category_display': message.get_category_display(),
                'status': message.status,
                'created_at': message.created_at.strftime('%d %b %Y - %H:%M'),
            }
        })
class MessageDeleteView(View):
    """POST /messages/<pk>/delete/  → supprime le message."""
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'error', 'message': 'Non authentifié'}, status=401)
        message = get_object_or_404(Message, pk=pk)
        message.delete()
        return JsonResponse({'status': 'success'})


class MessageArchiveView(View):
    """POST /messages/<pk>/archive/  → archive le message."""
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'error', 'message': 'Non authentifié'}, status=401)
        message = get_object_or_404(Message, pk=pk)
        message.status = 'archive'
        message.save()
        return JsonResponse({'status': 'success'})


class MessageReplyView(View):
    """POST /messages/<pk>/reply/  → envoie un e-mail de réponse."""
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'error', 'message': 'Non authentifié'}, status=401)
        message = get_object_or_404(Message, pk=pk)
        try:
            data = json.loads(request.body)
            subject = data.get('subject') or f"Re: {message.subject}"
            reply_body = data.get('message', '').strip()

            if not reply_body:
                return JsonResponse(
                    {'status': 'error', 'message': 'Le message ne peut pas être vide.'},
                    status=400
                )
            send_mail(
                subject=subject,
                message=reply_body,
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@kinerafilm.com'),
                recipient_list=[message.sender_email],
                fail_silently=False,
            )
            message.status = 'repondu'
            message.save()
            return JsonResponse({'status': 'success', 'message': 'Réponse envoyée avec succès!'})
        except Exception as exc:
            return JsonResponse({'status': 'error', 'message': str(exc)}, status=500)
