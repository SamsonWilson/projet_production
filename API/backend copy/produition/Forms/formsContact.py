from django import forms
from produition.models import Message
from django.core.exceptions import ValidationError


class MessageForm(forms.ModelForm):
    """
    Formulaire pour créer et envoyer des messages de contact.
    
    Ce formulaire valide et nettoie les données avant envoi.
    """
    
    class Meta:
        model = Message
        fields = ['sender_name', 'sender_email', 'sender_phone', 'subject', 'message', 'category']
        widgets = {
            'sender_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre nom complet',
                'required': True,
            }),
            'sender_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'votre.email@example.com',
                'required': True,
            }),
            'sender_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+33 6 XX XX XX XX (optionnel)',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sujet du message',
                'required': True,
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Écrivez votre message ici...',
                'rows': 8,
                'required': True,
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'required': True,
            }),
        }
        labels = {
            'sender_name': 'Nom complet *',
            'sender_email': 'Adresse email *',
            'sender_phone': 'Téléphone (optionnel)',
            'subject': 'Sujet *',
            'message': 'Votre message *',
            'category': 'Catégorie *',
        }

    def clean_sender_name(self):
        """Valider le nom du sender"""
        name = self.cleaned_data.get('sender_name', '').strip()
        
        if not name:
            raise ValidationError("Le nom est obligatoire.")
        
        if len(name) < 2:
            raise ValidationError("Le nom doit contenir au moins 2 caractères.")
        
        if len(name) > 100:
            raise ValidationError("Le nom ne peut pas dépasser 100 caractères.")
        
        return name

    def clean_sender_email(self):
        """Valider l'email du sender"""
        email = self.cleaned_data.get('sender_email', '').strip().lower()
        
        if not email:
            raise ValidationError("L'email est obligatoire.")
        
        return email

    def clean_subject(self):
        """Valider le sujet"""
        subject = self.cleaned_data.get('subject', '').strip()
        
        if not subject:
            raise ValidationError("Le sujet est obligatoire.")
        
        if len(subject) < 5:
            raise ValidationError("Le sujet doit contenir au moins 5 caractères.")
        
        if len(subject) > 200:
            raise ValidationError("Le sujet ne peut pas dépasser 200 caractères.")
        
        return subject

    def clean_message(self):
        """Valider le contenu du message"""
        message = self.cleaned_data.get('message', '').strip()
        
        if not message:
            raise ValidationError("Le message est obligatoire.")
        
        if len(message) < 10:
            raise ValidationError("Le message doit contenir au moins 10 caractères.")
        
        if len(message) > 5000:
            raise ValidationError("Le message ne peut pas dépasser 5000 caractères.")
        
        return message

    def clean(self):
        """Validation globale du formulaire"""
        cleaned_data = super().clean()
        
        # Vous pouvez ajouter des validations supplémentaires ici
        # Par exemple : vérifier si l'utilisateur a envoyé trop de messages récemment
        
        return cleaned_data
