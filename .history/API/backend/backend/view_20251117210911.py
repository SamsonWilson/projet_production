class ConnexionView(LoginView):
    template_name = 'registration/login.html'  # Ton template
    success_url = reverse_lazy('accueil')