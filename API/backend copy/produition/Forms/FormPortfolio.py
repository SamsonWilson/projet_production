from django import forms
from produition.models import PortfolioProject


class PortfolioProjectForm(forms.ModelForm):
    """
    Formulaire pour créer et modifier un projet portfolio.
    """

    class Meta:
        model = PortfolioProject
        fields = [
            'title',
            'description',
            'project_type',
            'category',
            'is_featured',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titre du projet'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Description du projet'
            }),

            'project_type': forms.Select(attrs={
                'class': 'form-control'
            }),

            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Mariage, Publicité, Corporate...'
            }),

            'is_featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

        labels = {
            'title': 'Titre *',
            'description': 'Description',
            'project_type': 'Type de réalisation *',
            'category': 'Catégorie',
            'is_featured': 'Mettre en avant',
        }

    # Validation titre
    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()

        if len(title) < 3:
            raise forms.ValidationError("Le titre doit contenir au moins 3 caractères.")

        return title



from produition.models import PortfolioMedia


class PortfolioMediaForm(forms.ModelForm):
    """
    Formulaire pour ajouter un média (image ou vidéo) à un projet.
    """

    class Meta:
        model = PortfolioMedia
        fields = ['media_type', 'file', 'thumbnail', 'order']

        widgets = {
            'media_type': forms.Select(attrs={
                'class': 'form-control'
            }),

            'file': forms.FileInput(attrs={
                'class': 'form-control'
            }),

            'thumbnail': forms.FileInput(attrs={
                'class': 'form-control'
            }),

            'order': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),
        }

        labels = {
            'media_type': 'Type de média',
            'file': 'Fichier',
            'thumbnail': 'Miniature (optionnel)',
            'order': 'Ordre d’affichage',
        }

    # Validation fichier obligatoire
    def clean_file(self):
        file = self.cleaned_data.get('file')

        if not file:
            raise forms.ValidationError("Le fichier est obligatoire.")

        return file