from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
class Message(models.Model):
    """Modèle pour stocker les messages de contact"""
    CATEGORY_CHOICES = [
        ('general', 'Général'),
        ('devis', 'Devis'),
        ('reclamation', 'Réclamation'),
        ('partenariat', 'Partenariat'),
    ]
    STATUS_CHOICES = [
        ('nouveau', 'Nouveau'),
        ('lu', 'Lu'),
        ('repondu', 'Répondu'),
        ('archive', 'Archivé'),
    ]
    # Informations de l'expéditeur
    sender_name = models.CharField(
        max_length=100,
        verbose_name="Nom de l'expéditeur"
    )
    sender_email = models.EmailField(
        validators=[EmailValidator()],
        verbose_name="Email de l'expéditeur"
    )
    sender_phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Téléphone"
    )
    
    # Contenu du message
    subject = models.CharField(
        max_length=200,
        verbose_name="Sujet"
    )
    message = models.TextField(
        verbose_name="Message"
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='general',
        verbose_name="Catégorie"
    )
    
    # Métadonnées
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='nouveau',
        verbose_name="Statut"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Date de modification"
    )
    read_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Date de lecture"
    )
    
    # Email d'envoi automatique
    email_sent = models.BooleanField(
        default=False,
        verbose_name="Email envoyé"
    )
    email_sent_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Date d'envoi de l'email"
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['status']),
            models.Index(fields=['sender_email']),
        ]
    
    def __str__(self):
        return f"{self.sender_name} - {self.subject}"
    
    def mark_as_read(self):
        """Marquer le message comme lu"""
        if not self.read_at:
            self.read_at = timezone.now()
            self.status = 'lu'
            self.save()

    @property
    def initials(self):
        """Retourne les initiales de l'expéditeur (ex: 'Jean Dupont' → 'JD')."""
        parts = self.sender_name.strip().split()
        if len(parts) >= 2:
            return f"{parts[0][0]}{parts[-1][0]}".upper()
        name = self.sender_name.strip()
        return name[:2].upper() if len(name) >= 2 else name.upper()

    @property
    def avatar_color(self):
        """Couleur d'avatar cyclique basée sur la clé primaire."""
        colors = ['', 'blue', 'green', 'red', 'orange']
        return colors[self.pk % len(colors)]


from django.db import models
from django.utils import timezone
from django.conf import settings


class Video(models.Model):
    """Modèle pour gérer les vidéos du site"""

    STATUS_CHOICES = [
        # on conserve le brouillon pour ne pas casser les données existantes
        ('draft', 'Brouillon'),
        ('published', 'Publié'),
        ('archived', 'Archivé'),
    ]

    CATEGORY_CHOICES = [
        ('hero', 'Héro'),
        ('portfolio', 'Portfolio'),
        ('about', 'À propos'),
        ('service', 'Services'),
        ('testimonial', 'Témoignage'),
        ('other', 'Autre'),
    ]

    # Informations principales
    title = models.CharField(
        max_length=200,
        verbose_name="Titre de la vidéo",
        default="Nouvelle vidéo"
    )

    description = models.TextField(
        blank=True,
        default="",
        verbose_name="Description"
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='other',
        verbose_name="Catégorie"
    )

    video_file = models.FileField(
        upload_to='videos/%Y/%m/',
        verbose_name="Fichier vidéo"
    )

    duration = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Durée (secondes)"
    )

    thumbnail = models.ImageField(
        upload_to='thumbnails/%Y/%m/',
        blank=True,
        null=True,
        verbose_name="Miniature"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
        verbose_name="Statut"
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="Mettre en avant"
    )

    custom_url = models.CharField(
        max_length=200,
        blank=True,
        unique=True,
        verbose_name="URL personnalisée"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    published_at = models.DateTimeField(
        blank=True,
        null=True
    )

    order = models.IntegerField(default=0)

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-order', '-created_at']
        verbose_name = "Vidéo"
        verbose_name_plural = "Vidéos"

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"

    def save(self, *args, **kwargs):
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        
        # Si cette vidéo est publiée et mise en avant,
        # les autres vidéos featured deviennent brouillon
        if self.status == 'published' and self.is_featured:
            Video.objects.filter(
                is_featured=True
            ).exclude(pk=self.pk).update(
                status='draft',
                is_featured=False
            )
        
        super().save(*args, **kwargs)

    @property
    def is_published(self):
        return self.status == 'published'



from django.db import models
from django.conf import settings


class PortfolioProject(models.Model):

    TYPE_CHOICES = [
        ('photo', 'Photographie'),
        ('video', 'Vidéo'),
        ('mixed', 'Photo & Vidéo'),
    ]

    title = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(blank=True, verbose_name="Description")

    project_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='photo',
        verbose_name="Type de réalisation"
    )

    category = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Catégorie"
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="Mettre en avant"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Projet Portfolio"
        verbose_name_plural = "Portfolio"

    def __str__(self):
        return self.title
    

class PortfolioMedia(models.Model):

    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Vidéo'),
    ]

    project = models.ForeignKey(
    PortfolioProject,
    related_name='medias',
    on_delete=models.CASCADE
)

    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_TYPE_CHOICES
    )

    file = models.FileField(
        upload_to='portfolio/%Y/%m/'
    )

    thumbnail = models.ImageField(
        upload_to='portfolio/thumbnails/%Y/%m/',
        blank=True,
        null=True
    )

    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} - {self.media_type}"    