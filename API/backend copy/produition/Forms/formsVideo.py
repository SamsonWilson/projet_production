from django import forms
from produition.models import Video


class VideoForm(forms.ModelForm):

    is_published = forms.BooleanField(
        required=False,
        label="Publié ?",
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )

    class Meta:
        model = Video
        fields = [
            'title',
            'description',
            'category',
            'video_file',
            'thumbnail',
            'is_featured',
            'duration',
            'custom_url',
            'order',
        ]

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titre de la vidéo'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
            }),
            'video_file': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'video/mp4,video/webm,video/ogg',
            }),
            'thumbnail': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'custom_url': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'order': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
        }

    # -------------------
    # Initialisation
    # -------------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['is_published'].initial = (
                self.instance.status == 'published'
            )

    # -------------------
    # Validation durée
    # -------------------
    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        if duration is not None and duration < 0:
            raise forms.ValidationError(
                "La durée doit être un nombre positif."
            )
        return duration

    # -------------------
    # Validation URL
    # -------------------
    def clean_custom_url(self):
        custom_url = self.cleaned_data.get('custom_url')

        if custom_url:
            qs = Video.objects.filter(custom_url=custom_url)

            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise forms.ValidationError(
                    "Cette URL est déjà utilisée."
                )

        return custom_url

    # -------------------
    # Validation vidéo
    # -------------------
    def clean_video_file(self):
        video = self.cleaned_data.get('video_file')

        if video:
            allowed_extensions = ['mp4', 'webm', 'ogg']
            ext = video.name.split('.')[-1].lower()

            if ext not in allowed_extensions:
                raise forms.ValidationError(
                    "Formats acceptés : MP4, WebM, OGG."
                )

        return video

    # -------------------
    # Validation globale
    # -------------------
    def clean(self):
        cleaned_data = super().clean()

        if not self.instance.pk and not cleaned_data.get('video_file'):
            self.add_error(
                'video_file',
                "Vous devez ajouter un fichier vidéo."
            )

        return cleaned_data

    # -------------------
    # Sauvegarde
    # -------------------
    def save(self, commit=True):
        instance = super().save(commit=False)

        # Gestion propre des statuts
        if self.cleaned_data.get('is_published'):
            instance.status = 'published'
        else:
            # Si pas publié → on garde brouillon
            instance.status = 'draft'

        if commit:
            instance.save()

        return instance


# from django import forms
# from produition.models import Video


# class VideoForm(forms.ModelForm):
#     """Formulaire pour créer et modifier les vidéos"""

#     # on remplace le statut par un champ booléen pour afficher un switch on/off
#     is_published = forms.BooleanField(
#         required=False,
#         label="Publié ?",
#         widget=forms.CheckboxInput(attrs={
#             'class': 'form-check-input',
#         })
#     )
#     class Meta:
#         model = Video
#         fields = [
#             'title',
#             'description',
#             'category',
#             'video_file',
#             'thumbnail',
#             # 'status' retiré, on gère via ``is_published``
#             'is_featured',
#             'duration',
#             'custom_url',
#             'order',
#         ]
#         widgets = {
#             'category': forms.Select(attrs={
#                 'class': 'form-control',
#             }),

#             'title': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Titre de la vidéo'
#             }),

#             'description': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'rows': 4,
#                 'placeholder': 'Description (optionnelle)'
#             }),

#             'video_file': forms.FileInput(attrs={
#                 'class': 'form-control',
#                 'accept': 'video/mp4,video/webm,video/ogg',
#             }),

#             'thumbnail': forms.FileInput(attrs={
#                 'class': 'form-control',
#                 'accept': 'image/*'
#             }),

#             # plus de widget pour 'status'

#             'is_featured': forms.CheckboxInput(attrs={
#                 'class': 'form-check-input',
#             }),

#             'duration': forms.NumberInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Durée en secondes',
#                 'min': '0'
#             }),

#             'custom_url': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'URL personnalisée (optionnel)'
#             }),

#             'order': forms.NumberInput(attrs={
#                 'class': 'form-control',
#                 'min': '0'
#             }),
#         }

#     # ✅ Validation individuelle de la durée
#     def clean_duration(self):
#         duration = self.cleaned_data.get('duration')
#         if duration is not None and duration < 0:
#             raise forms.ValidationError("La durée doit être un nombre positif.")
#         return duration
    
#     # ✅ Validation individuelle de l’URL
#     def clean_custom_url(self):
#         custom_url = self.cleaned_data.get('custom_url')

#         if custom_url:
#             qs = Video.objects.filter(custom_url=custom_url)

#             # Exclure l'objet actuel en cas de modification
#             if self.instance.pk:
#                 qs = qs.exclude(pk=self.instance.pk)

#             if qs.exists():
#                 raise forms.ValidationError("Cette URL est déjà utilisée.")

#         return custom_url

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # initialisation du bouton on/off à partir du statut existant
#         if self.instance and self.instance.pk:
#             self.fields['is_published'].initial = (self.instance.status == 'published')

#     # ✅ Validation globale (optionnel mais propre)
#     def clean(self):
#         cleaned_data = super().clean()

#         video_file = cleaned_data.get('video_file')

#         # Vérifier qu'une vidéo est fournie à la création
#         if not self.instance.pk and not video_file:
#             self.add_error('video_file', "Vous devez ajouter un fichier vidéo.")

#         # mapper le booléen vers le champ status avant de retourner
#         is_pub = cleaned_data.get('is_published')
#         cleaned_data['status'] = 'published' if is_pub else 'archived'

#         return cleaned_data

#     def save(self, commit=True):
#         # s'assurer que l'objet a le bon status
#         self.instance.status = 'published' if self.cleaned_data.get('is_published') else 'archived'
#         return super().save(commit)
    
#     def clean_video_file(self):
#         video = self.cleaned_data.get('video_file')

#         if video:
#             allowed_extensions = ['mp4', 'webm', 'ogg']
#             ext = video.name.split('.')[-1].lower()

#             if ext not in allowed_extensions:
#                 raise forms.ValidationError(
#                     "Formats acceptés : MP4, WebM, OGG."
#                 )

#         return video