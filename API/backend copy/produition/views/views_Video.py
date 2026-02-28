from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from produition.models import Video
from produition.Forms.formsVideo import VideoForm



class VideoListView(LoginRequiredMixin, ListView):
    model = Video
    template_name = 'Admin/Page_Backend/video_list.html'
    context_object_name = 'videos'
    paginate_by = 20
    login_url = 'connexion'

    def get_queryset(self):
        queryset = Video.objects.all().order_by('-order', '-created_at')
        status = self.request.GET.get('status')

        if status:
            queryset = queryset.filter(status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_filter'] = self.request.GET.get('status', '')
        return context


class VideoCreateView(LoginRequiredMixin, CreateView):
    """Créer une nouvelle vidéo"""
    model = Video
    form_class = VideoForm
    template_name = 'Admin/Page_Backend/video_form.html'
    success_url = reverse_lazy('video_list')
    login_url = 'connexion'

    def form_valid(self, form):
        # Associer l'utilisateur connecté
        form.instance.uploaded_by = self.request.user

        response = super().form_valid(form)

        messages.success(
            self.request,
            f'✓ Vidéo créée avec succès !'
        )

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Créer'
        context['page_title'] = 'Ajouter une nouvelle vidéo'
        return context


class VideoUpdateView(LoginRequiredMixin, UpdateView):
    """Modifier une vidéo existante."""

    model = Video
    form_class = VideoForm
    template_name = 'Admin/Page_Backend/video_form.html'
    success_url = reverse_lazy('video_list')
    login_url = 'connexion'

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(
            self.request,
            f'✓ Vidéo mise à jour avec succès !'
        )

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Modifier'

        # Afficher le nom du fichier vidéo au lieu de title
        if self.object.video_file:
            context['page_title'] = f"Modifier : {self.object.video_file.name}"
        else:
            context['page_title'] = "Modifier la vidéo"

        return context


class VideoDeleteView(LoginRequiredMixin, DeleteView):
    """Supprimer une vidéo."""
    model = Video
    template_name = 'Admin/Page_Backend/video_confirm_delete.html'
    success_url = reverse_lazy('video_list')
    login_url = 'connexion'
    
    def delete(self, request, *args, **kwargs):
        """Afficher un message de confirmation"""
        video_title = self.get_object().title
        messages.success(
            request,
            f'✓ Vidéo "{video_title}" supprimée avec succès!'
        )
        return super().delete(request, *args, **kwargs)


class VideoDetailView(DetailView):
    """Afficher les détails d'une vidéo."""
    model = Video
    template_name = 'Admin/Page_Backend/video_detail.html'
    context_object_name = 'video'
    def get_queryset(self):
        """Seules les vidéos publiées sont visibles au public"""
        return Video.objects.filter(status='published')


# ------------------------------------------------------------
# utilitaire pour basculer rapidement publié/archivé
# ------------------------------------------------------------
from django.views import View
from django.shortcuts import get_object_or_404


class VideoToggleStatusView(LoginRequiredMixin, View):
    """Basculer entre les deux états principaux (publié / archivé).

    Ce petit contrôleur est utilisé depuis la liste et la page de détail
    pour proposer un bouton on/off au lieu d'un texte.
    """

    def post(self, request, pk, *args, **kwargs):
        video = get_object_or_404(Video, pk=pk)

        # on ne gère que deux états, tout ce qui n'est pas 'published'
        # est considéré comme archivé pour le contexte de bascule
        if video.status == 'published':
            video.status = 'archived'
        else:
            video.status = 'published'

        video.save()
        messages.success(request, "Statut de la vidéo mis à jour.")

        # retour à la page précédente (ou à la liste si on ne sait pas)
        return redirect(request.META.get('HTTP_REFERER', reverse_lazy('video_list')))


class VideoToggleFeaturedView(LoginRequiredMixin, View):
    """Basculer l'indicateur `is_featured` pour une vidéo.

    Si on active la mise en avant et que la vidéo n'est pas publiée,
    on la publie automatiquement (comportement conservateur).
    """

    def post(self, request, pk, *args, **kwargs):
        video = get_object_or_404(Video, pk=pk)

        video.is_featured = not video.is_featured

        # si activation et pas encore publié, publier
        if video.is_featured and video.status != 'published':
            video.status = 'published'

        video.save()
        messages.success(request, "Mise en avant mise à jour.")

        return redirect(request.META.get('HTTP_REFERER', reverse_lazy('video_list')))


class HeroVideoView(ListView):
    """Afficher la vidéo héro (la vidéo récente avec statut 'hero' et 'published')"""
    model = Video
    template_name = 'Admin/Page_Backend/video_hero.html'
    context_object_name = 'video'
    
    def get_queryset(self):
        """Récupérer la vidéo héro la plus récente"""
        return Video.objects.filter(
            category='hero',
            status='published'
        ).order_by('-created_at')[:1]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        videos = list(self.get_queryset())
        context['video'] = videos[0] if videos else None
        return context
