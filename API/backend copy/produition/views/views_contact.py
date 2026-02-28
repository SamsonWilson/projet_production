from django.shortcuts import render, redirect
from django.contrib import messages as django_messages
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from django.conf import settings
from django.http import JsonResponse
import logging
from produition.models import Message
from produition.Forms.formsContact import MessageForm
from produition.models import Video

class ContactFormView(CreateView):
    """
    Vue pour traiter l'envoi des messages de contact.
    Flux:
    1. Reçoit le formulaire POST
    2. Valide les données
    3. Crée un objet Message en base de données
    4. Envoie un email de confirmation à l'expéditeur
    5. Envoie une notification à l'admin
    6. Retourne un message de succès
    """
    model = Message
    form_class = MessageForm
    template_name = 'dashboard/contact.html'
    success_url = reverse_lazy('contact')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # fournir au template la première vidéo publiée utilisée par l'hero
        context['videos'] = Video.objects.filter(status='published').order_by('-created_at')[:1]
        return context
    def form_valid(self, form):
        response = super().form_valid(form)
        # Tu peux ajouter un traitement ici (email automatique par exemple)
        return response