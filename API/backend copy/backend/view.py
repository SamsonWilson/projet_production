from django.views.generic import ListView, TemplateView
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
from produition.models import Message, Video, PortfolioMedia
from produition.Forms.formsContact import MessageForm


class BaseVideoContextMixin:
    """Mixin pour passer les vidéos et images du portfolio au contexte de tous les templates"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Récupérer les vidéos publiées avec featured=True pour la vidéo héro
        context['videos'] = Video.objects.filter(
            status='published',
            is_featured=True
        ).order_by('-order')[:1]  # Prendre la première (la plus importante)
        
        # Récupérer TOUTES les images du portfolio
        context['portfolio_images'] = PortfolioMedia.objects.filter(
            media_type='image'
        ).order_by('order')
        
        # Récupérer TOUTES les vidéos du portfolio
        context['portfolio_videos'] = PortfolioMedia.objects.filter(
            media_type='video'
        ).order_by('order')
        
        return context


class index(BaseVideoContextMixin, TemplateView):
    template_name = 'dashboard/accueil.html'


class service(BaseVideoContextMixin, TemplateView):
    template_name = 'dashboard/service.html'


class about(BaseVideoContextMixin, TemplateView):
    template_name = 'dashboard/about.html'    


class portfolio(BaseVideoContextMixin, TemplateView):
    template_name = 'dashboard/Portfolio.html'

class contactbase(BaseVideoContextMixin, TemplateView):
    template_name = 'dashboard/contact.html'


class HomeView(ListView):
    model = Video
    template_name = "dashboard/base.html"
    context_object_name = "videos"
    
    def get_queryset(self):
        return Video.objects.filter(
            status='published',
            is_featured=True
        ).order_by('-order')

logger = logging.getLogger(__name__)
def send_email_to_sender(message_obj, request):
    """
    Envoie un email de confirmation à l'expéditeur.
    
    Paramètres:
        - message_obj: L'objet Message envoyé
        - request: La requête HTTP pour construire les URLs absolues
    
    Retour:
        - bool: True si l'email a été envoyé avec succès, False sinon
    """
    try:
        # Préparer le contexte pour le template d'email
        context = {
            'sender_name': message_obj.sender_name,
            'subject': message_obj.subject,
            'message': message_obj.message,
            'category': message_obj.get_category_display(),
            'date': message_obj.created_at,
            'message_id': message_obj.id,
            'site_name': 'KINÉRA FILM FIXERS',
            'site_url': request.build_absolute_uri('/'),
        }
        
        # Générer le contenu HTML de l'email
        html_content = render_to_string('emails/message_confirmation.html', context)
        text_content = strip_tags(html_content)
        
        # Créer l'email avec contenu texte et HTML
        email = EmailMultiAlternatives(
            subject=f"✓ Confirmation - Votre message a été reçu (#{message_obj.id})",
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[message_obj.sender_email]
        )
        
        # Attacher la version HTML
        email.attach_alternative(html_content, "text/html")
        
        # Envoyer l'email
        email.send(fail_silently=False)
        
        # Mettre à jour les métadonnées
        message_obj.email_sent = True
        message_obj.email_sent_at = timezone.now()
        message_obj.save()
        
        logger.info(f"Email de confirmation envoyé à {message_obj.sender_email} pour le message #{message_obj.id}")
        return True
        
    except Exception as e:
        logger.error(f"Erreur lors de l'envoi de l'email à {message_obj.sender_email}: {str(e)}")
        return False


def send_email_to_admin(message_obj, request):
    """
    Envoie un email de notification à l'administrateur.
    
    Paramètres:
        - message_obj: L'objet Message reçu
        - request: La requête HTTP
    
    Retour:
        - bool: True si l'email a été envoyé avec succès
    """
    try:
        context = {
            'sender_name': message_obj.sender_name,
            'sender_email': message_obj.sender_email,
            'sender_phone': message_obj.sender_phone,
            'subject': message_obj.subject,
            'message': message_obj.message,
            'category': message_obj.get_category_display(),
            'date': message_obj.created_at,
            'message_id': message_obj.id,
            'admin_url': request.build_absolute_uri(f'/admin/produition/message/{message_obj.id}/change/'),
        }
        
        html_content = render_to_string('emails/message_admin_notification.html', context)
        text_content = strip_tags(html_content)
        
        email = EmailMultiAlternatives(
            subject=f"🔔 Nouveau message reçu: {message_obj.subject} (#{message_obj.id})",
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.ADMIN_EMAIL] if hasattr(settings, 'ADMIN_EMAIL') else [admin[1] for admin in settings.ADMINS]
        )
        
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)
        
        logger.info(f"Email d'administration envoyé pour le message #{message_obj.id}")
        return True
        
    except Exception as e:
        logger.error(f"Erreur lors de l'envoi de l'email admin: {str(e)}")
        return False


class ContactFormView(BaseVideoContextMixin, CreateView):
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
    
    def form_valid(self, form):
        """Traiter le formulaire valide"""
        # Sauvegarder le message en base de données
        message = form.save()
        
        try:
            # Envoyer l'email de confirmation à l'expéditeur
            sender_email_sent = send_email_to_sender(message, self.request)
            
            # Envoyer une notification à l'admin
            admin_email_sent = send_email_to_admin(message, self.request)
            
            # Message de succès
            if sender_email_sent and admin_email_sent:
                django_messages.success(
                    self.request,
                    f"✓ Merci {message.sender_name}! Votre message a été reçu avec succès. "
                    f"Un email de confirmation a été envoyé à {message.sender_email}."
                )
            elif sender_email_sent:
                django_messages.success(
                    self.request,
                    f"✓ Votre message a été reçu! Un email de confirmation vous a été envoyé."
                )
            else:
                django_messages.warning(
                    self.request,
                    f"✓ Votre message a été enregistré, mais l'envoi de l'email de confirmation a échoué."
                )
                
        except Exception as e:
            logger.error(f"Erreur lors du traitement du formulaire de contact: {str(e)}")
            django_messages.error(
                self.request,
                "Une erreur s'est produite lors de l'envoi de votre message. Veuillez réessayer."
            )
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Gérer les erreurs de formulaire"""
        # Retourner le formulaire avec les erreurs
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        """Ajouter le formulaire au contexte"""
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            context['form'] = MessageForm()
        return context


# Vue alternative avec gestion AJAX (optionnel)
def send_message_ajax(request):
    """
    Vue AJAX pour envoyer des messages sans rechargement de page.
    
    Retour: JSON {success: bool, message: str}
    """
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        
        if form.is_valid():
            message = form.save()
            
            try:
                send_email_to_sender(message, request)
                send_email_to_admin(message, request)
                
                return JsonResponse({
                    'success': True,
                    'message': f"Merci! Votre message a été reçu avec succès.",
                    'message_id': message.id
                })
            except Exception as e:
                logger.error(f"Erreur AJAX: {str(e)}")
                return JsonResponse({
                    'success': False,
                    'message': "Une erreur s'est produite lors de l'envoi."
                }, status=500)
        else:
            # Retourner les erreurs du formulaire
            errors = {field: [str(error) for error in error_list] 
                     for field, error_list in form.errors.items()}
            return JsonResponse({
                'success': False,
                'message': "Le formulaire contient des erreurs.",
                'errors': errors
            }, status=400)
    
    return JsonResponse({'success': False, 'message': 'Méthode non autorisée'}, status=405)
