from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from produition.models import CustomUser


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        label='Prénom',
        widget=forms.TextInput(attrs={'placeholder': 'Votre prénom'})
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        label='Nom',
        widget=forms.TextInput(attrs={'placeholder': 'Votre nom'})
    )
    email = forms.EmailField(
        required=True,
        label='Adresse e-mail',
        widget=forms.EmailInput(attrs={'placeholder': 'exemple@email.com'})
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        label='Téléphone',
        widget=forms.TextInput(attrs={'placeholder': '+221 XX XXX XX XX'})
    )
    password1 = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'placeholder': 'Créez un mot de passe'})
    )
    password2 = forms.CharField(
        label='Confirmer le mot de passe',
        widget=forms.PasswordInput(attrs={'placeholder': 'Répétez le mot de passe'})
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}),
        }
        labels = {
            'username': "Nom d'utilisateur",
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Cette adresse e-mail est déjà utilisée.")
        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur ou e-mail"})
    )
    password = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'placeholder': 'Votre mot de passe'})
    )
