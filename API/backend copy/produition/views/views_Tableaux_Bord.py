from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class AdminView(LoginRequiredMixin, TemplateView):
    """Tableau de bord admin - accès réservé aux utilisateurs connectés."""
    template_name = 'Admin/Page_Backend/Tableaux_Bord.html'
    login_url = 'connexion'
