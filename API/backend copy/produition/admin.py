from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from produition.models import CustomUser, Message, Video
from django.contrib import admin
from django.utils.html import format_html
from .models import Video

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Administration personnalisée des utilisateurs."""
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'is_active', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone')
    ordering = ('-date_joined',)

    fieldsets = UserAdmin.fieldsets + (
        ('Informations supplémentaires', {
            'fields': ('phone',)
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informations supplémentaires', {
            'fields': ('email', 'first_name', 'last_name', 'phone')
        }),
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Administration des messages de contact."""
    list_display = ('sender_name', 'sender_email', 'subject', 'category', 'status', 'email_sent', 'created_at')
    list_filter = ('status', 'category', 'email_sent', 'created_at')
    search_fields = ('sender_name', 'sender_email', 'subject')
    readonly_fields = ('email_sent', 'email_sent_at', 'created_at', 'updated_at', 'read_at')
    
    fieldsets = (
        ('Informations Expéditeur', {
            'fields': ('sender_name', 'sender_email', 'sender_phone')
        }),
        ('Contenu', {
            'fields': ('subject', 'message', 'category')
        }),
        ('Statut', {
            'fields': ('status', 'read_at')
        }),
        ('Email', {
            'fields': ('email_sent', 'email_sent_at'),
            'classes': ('collapse',)
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'category',
        'status',
        'is_featured',
        'order',
        'duration',
        'created_at'
    )

    list_filter = (
        'status',
        'category',
        'is_featured',
        'created_at'
    )

    search_fields = (
        'custom_url',
        'video_file'
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'published_at',
        'video_preview'
    )

    ordering = ('-order', '-created_at')

    list_editable = ('status', 'is_featured', 'order')

    fieldsets = (
        ('Informations principales', {
            'fields': ('category',)
        }),

        ('Fichiers média', {
            'fields': ('video_file', 'thumbnail', 'video_preview')
        }),

        ('Métadonnées', {
            'fields': ('duration', 'order')
        }),

        ('Publication', {
            'fields': ('status', 'is_featured', 'published_at')
        }),

        ('URL', {
            'fields': ('custom_url',),
            'classes': ('collapse',)
        }),

        ('Gestion', {
            'fields': ('uploaded_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def video_preview(self, obj):
        if obj.video_file:
            return format_html(
                '<video width="300" controls>'
                '<source src="{}" type="video/mp4"></video>'
                '</video>',
                obj.video_file.url
            )
        return "Aucune vidéo"

    video_preview.short_description = "Aperçu vidéo"

    def save_model(self, request, obj, form, change):
        if not change:
            obj.uploaded_by = request.user
        super().save_model(request, obj, form, change)