from produition.Forms.FormPortfolio import PortfolioMediaForm
from produition.models import PortfolioMedia
from django.views.generic import (ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from produition.models import PortfolioProject
from produition.Forms.FormPortfolio import PortfolioProjectForm


class PortfolioMediaCreateView(LoginRequiredMixin, CreateView):
    model = PortfolioMedia
    form_class = PortfolioMediaForm
    template_name = 'Admin/Page_Backend/Portfolios_media/portfolio_media_form.html'

    def form_valid(self, form):
        project_id = self.kwargs.get('project_id')
        form.instance.project_id = project_id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('portfolio_detail', kwargs={'pk': self.object.project.pk})
    

class PortfolioMediaDeleteView(LoginRequiredMixin, DeleteView):
    model = PortfolioMedia

    def get_success_url(self):
        return reverse_lazy(
            'portfolio_detail',
            kwargs={'pk': self.object.project.pk}
        )    
    

class PortfolioMediaListView(ListView):
    model = PortfolioMedia
    template_name = 'Admin/Page_Backend/Portfolios_media/list.html'
    context_object_name = 'medias'
    paginate_by = 12

    # def get_queryset(self):
    #     return PortfolioMedia.objects.all().order_by('-created_at')
    
