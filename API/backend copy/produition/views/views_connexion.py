from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect

from produition.Forms.formsAuth import RegisterForm, LoginForm


class CustomLoginView(LoginView):
    """Vue de connexion personnalisée avec redirection automatique."""
    template_name = 'Admin/connexion/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tableau_de_bord')


class InscriptionView(CreateView):
    """Vue d'inscription : crée l'utilisateur et le connecte automatiquement."""
    template_name = 'Admin/connexion/signup.html'
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        # Redirige si déjà connecté
        if request.user.is_authenticated:
            return redirect(reverse_lazy('connexion'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        # Connexion automatique après inscription
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(reverse_lazy('connexion'))


class CustomLogoutView(LogoutView):
    """Vue de déconnexion avec redirection vers la page de connexion."""
    next_page = reverse_lazy('connexion')
    http_method_names = ['get', 'post']
