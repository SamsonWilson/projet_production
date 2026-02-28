from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from produition.models import PortfolioProject
from produition.Forms.FormPortfolio import PortfolioProjectForm


class PortfolioListView(ListView):
    model = PortfolioProject
    template_name = 'Admin/Page_Backend/Portfolios/portfolio_list.html'
    context_object_name = 'projects'
    paginate_by = 12

    def get_queryset(self):
        return PortfolioProject.objects.all().order_by('-is_featured', '-created_at')
    


# class PortfolioDetailView(DetailView):
#         model = PortfolioProject
#         template_name = 'Admin/Page_Backend/Portfolios/portfolio_detail.html'
#         context_object_name = 'project'

class PortfolioDetailView(DetailView):
    model = PortfolioProject
    template_name = 'Admin/Page_Backend/Portfolios/portfolio_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        medias = list(self.object.medias.all().order_by('order'))

        # Détecter de façon robuste si le fichier est une vidéo d'après l'extension
        video_ext = ('.mp4', '.webm', '.ogg', '.mov', '.mkv')
        for m in medias:
            name = (m.file.name or '').lower()
            is_vid = any(name.endswith(ext) for ext in video_ext)
            # expose both `_is_video` (internal) and `is_video` (used by some templates)
            m._is_video = is_vid
            m.is_video = is_vid

        context['medias'] = medias
        return context

class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = PortfolioProject
    form_class = PortfolioProjectForm
    template_name = 'Admin/Page_Backend/Portfolios/portfolio_form.html'
    success_url = reverse_lazy('portfolio_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        # Si on met en avant → retirer les autres featured
        if form.cleaned_data.get('is_featured'):
            PortfolioProject.objects.filter(
                is_featured=True
            ).update(is_featured=False)

        return super().form_valid(form)    
    

class PortfolioUpdateView(LoginRequiredMixin, UpdateView):
    model = PortfolioProject
    form_class = PortfolioProjectForm
    template_name = 'Admin/Page_Backend/Portfolios/portfolio_form.html'
    success_url = reverse_lazy('portfolio_list')

    def form_valid(self, form):
        if form.cleaned_data.get('is_featured'):
            PortfolioProject.objects.filter(
                is_featured=True
            ).exclude(pk=self.object.pk).update(is_featured=False)

        return super().form_valid(form)



class PortfolioDeleteView(LoginRequiredMixin, DeleteView):
    model = PortfolioProject
    template_name = 'Admin/Page_Backend/Portfolios/portfolio_confirm_delete.html'
    success_url = reverse_lazy('portfolio_list')        