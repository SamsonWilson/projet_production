# 📹 Gestion des Vidéos - Documentation Complète

## Vue d'ensemble

Un système complet pour gérer les vidéos du site a été créé. Vous pouvez désormais ajouter, modifier, supprimer et afficher les vidéos facilement via l'interface web ou l'administration Django.

---

## ✨ Fonctionnalités

- ✅ **Créer** des vidéos avec titre, description, catégorie
- ✅ **Modifier** les vidéos existantes
- ✅ **Supprimer** les vidéos (avec confirmation)
- ✅ **Afficher** les détails complets d'une vidéo
- ✅ **Lister** toutes les vidéos avec pagination
- ✅ **Filtrer** par statut (Publié, Brouillon, Archivé)
- ✅ **Télécharger** des fichiers vidéo (MP4, WebM, OGG)
- ✅ **Ajouter** des miniatures (thumbnails)
- ✅ **Gérer** la publication en administration Django
- ✅ **Tracer** les métadonnées (créateur, dates, etc.)

---

## 🗄️ Modèle de Base de Données

### Modèle `Video`

```python
class Video(models.Model):
    # Informations principales
    title              - CharField          # Titre de la vidéo
    description        - TextField          # Description détaillée
    category           - CharField          # Catégorie (hero, portfolio, about, etc.)
    
    # Fichiers
    video_file         - FileField          # Fichier vidéo (MP4, WebM, OGG)
    thumbnail          - ImageField         # Image de miniature
    
    # Métadonnées vidéo
    duration           - IntegerField       # Durée en secondes
    
    # État et publication
    status             - CharField          # draft, published, archived
    is_featured        - BooleanField       # Vidéo en avant (mise en avant)
    published_at       - DateTimeField      # Date de publication
    
    # Gestion
    custom_url         - CharField          # URL personnalisée
    order              - IntegerField       # Ordre d'affichage
    uploaded_by        - ForeignKey(User)   # Utilisateur qui a uploadé
    created_at         - DateTimeField      # Date de création
    updated_at         - DateTimeField      # Date de modification
```

### Catégories disponibles
- `hero` - Vidéo d'accueil/héro
- `portfolio` - Portfolio/projets
- `about` - À propos
- `service` - Services
- `testimonial` - Témoignages
- `other` - Autre

### Statuts de publication
- `draft` - Brouillon (non publié)
- `published` - Publié (visible)
- `archived` - Archivé (caché)

---

## 🚀 Utilisation

### 1️⃣ Via l'Interface Web

#### Accéder à la gestion des vidéos
```
URL: /videos/
Perms: Connecté
```

#### Ajouter une vidéo
```
1. Allez sur: /videos/
2. Cliquez sur "Ajouter une vidéo"
3. Remplissez le formulaire:
   - Titre (obligatoire)
   - Description
   - Catégorie
   - Fichier vidéo (obligatoire)
   - Miniature (optionnelle)
   - Statut (draft/published/archived)
   - Mise en avant (oui/non)
   - Durée en secondes
   - Ordre d'affichage
4. Cliquez sur "Créer"
```

#### Modifier une vidéo
```
1. Allez sur: /videos/
2. Trouvez la vidéo à modifier
3. Cliquez sur l'icône Modifier (crayon)
4. Modifiez les informations
5. Cliquez sur "Modifier"
```

#### Supprimer une vidéo
```
1. Allez sur: /videos/
2. Trouvez la vidéo à supprimer
3. Cliquez sur l'icône Supprimer (corbeille)
4. Confirmez la suppression
```

#### Filtrer les vidéos
```
- Tous: affiche toutes les vidéos
- Publiés: affiche les vidéos publiées
- Brouillons: affiche les brouillons
- Archivés: affiche les vidéos archivées
```

---

### 2️⃣ Via l'Administration Django

#### Accéder à l'admin
```
URL: /admin/
```

#### Ajouter/Modifier une vidéo dans l'admin
```
1. Allez sur: /admin/produition/video/
2. Cliquez sur "Ajouter Vidéo"
3. Remplissez les champs:
   - Informations principales
   - Fichiers Media
   - Métadonnées Vidéo
   - Publication
   - URL personnalisée (montrant aussi les erreurs)
   - Gestion
4. Cliquez sur "ENREGISTRER"
```

**Fonctionnalités spéciales en admin:**
- ✅ Édition en ligne de la liste (status, featured, order)
- ✅ Aperçu vidéo directement dans l'admin
- ✅ Filtres par statut, catégorie, featured, date
- ✅ Recherche par titre, description, URL
- ✅ Champs en lecture seule (dates créées/modifiées)

---

## 🔗 URLs disponibles

| URL | Vue | Description |
|-----|-----|-------------|
| `/videos/` | `VideoListView` | Lista les vidéos |
| `/videos/ajouter/` | `VideoCreateView` | Ajoute une nouvelle vidéo |
| `/videos/<id>/` | `VideoDetailView` | Voir les détails |
| `/videos/<id>/modifier/` | `VideoUpdateView` | Modifier une vidéo |
| `/videos/<id>/supprimer/` | `VideoDeleteView` | Supprimer une vidéo |
| `/videos/hero/` | `HeroVideoView` | Afficher la vidéo héro |
| `/admin/produition/video/` | Django Admin | Interface d'administration |

---

## 💾 Fichiers créés/modifiés

### Modèles
- ✅ `produition/models.py` - Ajout du modèle `Video`

### Formulaires
- ✅ `produition/Forms/formsVideo.py` - Nouveau formulaire CRUD

### Vues
- ✅ `produition/views/views_Video.py` - Toutes les vues CRUD

### URLs
- ✅ `produition/urls.py` - Routes pour les vidéos

### Admin
- ✅ `produition/admin.py` - Enregistrement du modèle en admin

### Templates
- ✅ `templates/Admin/Page_Backend/video_list.html` - Liste des vidéos
- ✅ `templates/Admin/Page_Backend/video_form.html` - Formulaire CRUD
- ✅ `templates/Admin/Page_Backend/video_detail.html` - Détails
- ✅ `templates/Admin/Page_Backend/video_confirm_delete.html` - Confirmation suppression

### Migrations
- ✅ `produition/migrations/0003_video.py` - Migration pour la table Video

---

## 🎯 Exemples d'utilisation

### Exemple 1: Ajouter une vidéo de portfolio

```
Titre: "Campagne Hyundai 2025"
Description: "Réalisation commerciale pour Hyundai avec tournage en Afrique de l'Ouest"
Catégorie: Portfolio
Fichier: hyundai_campaign.mp4
Miniature: hyundai_thumb.jpg
Statut: Publié
Mise en avant: Oui
Durée: 120
Ordre: 1
```

### Exemple 2: Créer une vidéo héro

```
Titre: "KINÉRA Production Services"
Description: "Bienvenue chez KINÉRA - Votre partenaire de production en Afrique"
Catégorie: Héro
Fichier: hero_video.mp4
Miniature: hero_thumb.jpg
Statut: Publié
Mise en avant: Non
Durée: 30
Ordre: 0
```

### Exemple 3: Témoignage client

```
Titre: "Témoignage Netflix"
Description: "Retours d'expérience de Netflix sur nos services"
Catégorie: Témoignage
Fichier: netflix_testimonial.mp4
Miniature: netflix_thumb.jpg
Statut: Brouillon (en attente de validation)
Mise en avant: Non
```

---

## 🛡️ Permissions

Les vues sont protégées:
- ✅ Login requis pour lister, ajouter, modifier, supprimer
- ✅ La vidéo héro est publique (affiche les vidéos publiées uniquement)
- ✅ Le détail des vidéos est visible uniquement si statut = "published"

---

## 🔧 Intégration avec templates

### Afficher la vidéo héro
```django
{% include 'Admin/Page_Backend/video_hero.html' %}
```

### Afficher une vidéo spécifique
```django
{% load static %}
{% if video %}
    <video width="100%" controls>
        <source src="{{ video.video_file.url }}" type="video/mp4">
    </video>
{% endif %}
```

---

## 📝 Notes importantes

1. **Les fichiers vidéo** sont sauvegardés dans `media/videos/YYYY/MM/`
2. **Les miniatures** sont sauvegardées dans `media/thumbnails/YYYY/MM/`
3. **Les formats acceptés** pour vidéo: MP4, WebM, OGG
4. **Taille maximale** dépend de votre configuration Django (modifiable)
5. **L'ordre d'affichage** est utilisé pour trier les vidéos (0 = première)

---

## ⚙️ Configuration (optionnelle)

### Augmenter la limite de taille de fichier

Dans `backend/settings.py`:
```python
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5 MB
```

### Configurer le dossier de stockage

Les fichiers vont automatiquement à `/media/videos/` et `/media/thumbnails/`

---

## 🎓 Tutoriel rapide

1. **Démarrer le serveur** Django
2. **Se connecter** à `/admin/`
3. **Aller à:** Produition > Vidéos
4. **Cliquer:** "Ajouter Vidéo"
5. **Remplir** le formulaire
6. **Cliquer:** "ENREGISTRER"
7. **Voilà!** Votre vidéo est créée

---

## 🆘 Dépannage

### Erreur "Aucune vidéo trouvée"
→ Assurez-vous que des vidéos existent et sont publiées (status = 'published')

### Erreur d'upload de fichier
→ Vérifiez que le dossier `/media/` existe et a les bonnes permissions

### Problème de permissions
→ Assurez-vous d'être connecté avec un compte staff/admin

---

## 📞 Besoin d'aide?

Consultez la documentation Django ou contactez l'équipe de développement.

---

**Dernière mise à jour:** 24 Février 2026
**Version:** 1.0
