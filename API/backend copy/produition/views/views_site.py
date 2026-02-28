from django.views.generic import ListView, DetailView
from produition.models import PortfolioProject


class PortfolioListView(ListView):
    model = PortfolioProject
    template_name = 'portfolio/list.html'
    context_object_name = 'items'
    paginate_by = 12

    def get_queryset(self):
        return PortfolioProject.objects.filter(published=True)


class PortfolioDetailView(DetailView):
    model = PortfolioProject
    template_name = 'portfolio/detail.html'
    context_object_name = 'item'

    def get_queryset(self):
        return PortfolioProject.objects.filter(published=True)