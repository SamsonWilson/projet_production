# 📧 SYSTÈME D'ENVOI DE MESSAGES AVEC EMAILS - GUIDE COMPLET

## 🎯 Vue d'ensemble du système

Ce système capture les messages de contact et envoie automatiquement des emails :
1. **Email de confirmation** au client (expéditeur)
2. **Email de notification** à l'administrateur (avec lien direct d'action)

---

## 📁 Architecture du système

```
projet_production/
├── API/backend/
│   ├── produition/
│   │   ├── models.py                 # Modèle Message
│   │   ├── Forms/
│   │   │   └── formsContact.py       # Formulaire de validation
│   │   ├── views/
│   │   │   └── views_contact.py      # Vue de traitement + envoi email
│   │   └── urls.py                   # URLs pour le contact
│   ├── templates/
│   │   ├── dashboard/
│   │   │   └── contact.html          # Formulaire frontend
│   │   └── emails/
│   │       ├── message_confirmation.html    # Email client
│   │       └── message_admin_notification.html # Email admin
│   ├── backend/
│   │   └── settings.py               # Configuration email
│   └── manage.py
```

---

## 🔧 COMPOSANTS DÉTAILLÉS

### 1️⃣ MODÈLE MESSAGE (models.py)

```python
class Message(models.Model):
    # Infos expéditeur
    sender_name = CharField()
    sender_email = EmailField()
    sender_phone = CharField(optional)
    
    # Contenu
    subject = CharField()
    message = TextField()
    category = CharField(choices=[general, devis, reclamation, partenariat])
    
    # Métadonnées
    status = CharField(choices=[nouveau, lu, repondu, archive])
    created_at = DateTimeField()
    read_at = DateTimeField(nullable)
    
    # Email
    email_sent = BooleanField(default=False)
    email_sent_at = DateTimeField(nullable)
```

**Champs importants:**
- `email_sent`: Vérifie si l'email a été envoyé avec succès
- `email_sent_at`: Enregistre quand l'email a été envoyé
- `status`: Permet de gérer le workflow (nouveau → lu → repondu)

---

### 2️⃣ FORMULAIRE (formsContact.py)

Le formulaire valide les données AVANT l'envoi:

```python
class MessageForm(ModelForm):
    """Validation côté serveur"""
    
    - sender_name: 2-100 caractères
    - sender_email: Format email valide
    - subject: 5-200 caractères
    - message: 10-5000 caractères
    - category: Choix prédéfini
```

**Validations personnalisées:**
- Pas de champs vides
- Longueur minimale/maximale
- Format email strict
- Prévention du spam

---

### 3️⃣ VUES (views_contact.py)

#### **Fonction: send_email_to_sender()**
Envoie un email de confirmation au CLIENT

```
ENTRÉE: Message object, request HTTP
│
├─ Préparer contexte (nom, sujet, date, etc.)
├─ Render template HTML: message_confirmation.html
├─ Créer EmailMultiAlternatives (texte + HTML)
├─ Envoyer via settings.EMAIL_*
├─ Mettre à jour message.email_sent = True
└─ Logger le succès/erreur

SORTIE: Boolean (succès/échec)
```

#### **Fonction: send_email_to_admin()**
Envoie une notification à l'ADMINISTRATEUR

```
ENTRÉE: Message object, request HTTP
│
├─ Préparer contexte (contact, catégorie, lien admin)
├─ Render template HTML: message_admin_notification.html
├─ Créer EmailMultiAlternatives
├─ Envoyer à settings.ADMIN_EMAIL
└─ Logger le succès/erreur

SORTIE: Boolean (succès/échec)
```

#### **Vue: ContactFormView** (CreateView)

```
FLUX D'EXÉCUTION:
┌─────────────────────────────────────────┐
│ 1. GET request → Afficher le formulaire │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│ 2. POST request → Recevoir les données  │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│ 3. Valider avec MessageForm             │
│    - Nettoyer les données               │
│    - Vérifier les formats               │
└─────────────────────────────────────────┘
                    ↓
         ❌ ERREURS? → Afficher le formulaire
                    ↓ ✅ VALIDE
┌─────────────────────────────────────────┐
│ 4. Sauvegarder en base de données       │
│    message.save()                       │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│ 5. Envoyer email de confirmation CLIENT │
│    send_email_to_sender()               │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│ 6. Envoyer notification à l'ADMIN       │
│    send_email_to_admin()                │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│ 7. Afficher message de succès           │
│ 8. Rediriger vers contact.html          │
└─────────────────────────────────────────┘
```

---

### 4️⃣ TEMPLATES D'EMAILS

#### **message_confirmation.html** (Email CLIENT)
- ✓ Header avec gradient orange KINÉRA
- ✓ Message de bienvenue personnalisé
- ✓ Résumé du message envoyé
- ✓ N° de ticket unique (#ID)
- ✓ Étapes suivantes
- ✓ Bouton de retour site
- ✓ Responsive design

**Contexte nécessaire:**
```python
{
    'sender_name': 'Jean Dupont',
    'subject': 'Demande de devis',
    'message': 'Contenu du message...',
    'category': 'Devis',
    'date': datetime,
    'message_id': 123,
    'site_name': 'KINÉRA FILM FIXERS',
    'site_url': 'https://kinera.com'
}
```

#### **message_admin_notification.html** (Email ADMIN)
- ✓ Header noir/orange professionnel
- ✓ Info rapide: De, Email, Téléphone
- ✓ Catégorie en évidence
- ✓ Sujet mis en avant
- ✓ Corps du message en zone grise
- ✓ Alerte spéciale pour "Réclamation"
- ✓ Boutons actions: "Voir dans l'admin", "Répondre"
- ✓ N° de ticket pour suivi

**Contexte nécessaire:**
```python
{
    'sender_name': 'Jean Dupont',
    'sender_email': 'jean@email.com',
    'sender_phone': '+33612345678',
    'subject': 'Demande urgente',
    'message': 'Contenu complet...',
    'category': 'Reclamation',  # Déclenche l'alerte
    'date': datetime,
    'message_id': 123,
    'admin_url': '/admin/produition/message/123/change/'
}
```

---

## ⚙️ CONFIGURATION DJANGO

### settings.py - Configuration Email

#### **POUR LE DÉVELOPPEMENT** (Console):
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Les emails s'affichent dans la console Django
```

#### **POUR LA PRODUCTION** (Gmail):
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre-email@gmail.com'
EMAIL_HOST_PASSWORD = 'application-password'  # Pas votre mdp Gmail!
DEFAULT_FROM_EMAIL = 'contact@kinera-filmfixers.com'
ADMIN_EMAIL = 'admin@kinera-filmfixers.com'
```

#### **POUR UN SERVEUR SMTP PERSONNALISÉ**:
```python
EMAIL_HOST = 'smtp.votreserveur.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'support@votredomaine.com'
EMAIL_HOST_PASSWORD = 'votre-mot-de-passe'
```

### Logging
```python
# Logs sauvegardés dans /backend/logs/email.log
LOGGING = {
    'loggers': {
        'produition.views.views_contact': {
            'level': 'INFO',
            'handlers': ['file', 'console']
        }
    }
}
```

---

## 🔗 CONFIGURATION DES URLS

### produition/urls.py

```python
from produition.views.views_contact import ContactFormView, send_message_ajax

urlpatterns = [
    # Formulaire contact (GET/POST traditionnel)
    path('contact/', ContactFormView.as_view(), name='contact'),
    
    # API AJAX pour JS (optionnel)
    path('api/send-message/', send_message_ajax, name='send_message_ajax'),
]
```

---

## 📤 FLUX COMPLET D'UN MESSAGE

```
CLIENT REMPLIT FORMULAIRE
        ↓
   ┌────────────────────────────────────────┐
   │ form.is_valid()                        │
   │ Validation du formulaire               │
   └────────────────────────────────────────┘
        ↓ ✅
   ┌────────────────────────────────────────┐
   │ Message.objects.create()               │
   │ Sauvegarde en base de données          │
   │ ID généré automatiquement              │
   └────────────────────────────────────────┘
        ↓
   ┌────────────────────────────────────────┐
   │ send_email_to_sender()                 │
   │ Envoyer confirmation au CLIENT         │
   │ ✓ Template HTML                        │
   │ ✓ N° de ticket #123                    │
   │ ✓ Informations personnalisées          │
   └────────────────────────────────────────┘
        ↓
   ┌────────────────────────────────────────┐
   │ send_email_to_admin()                  │
   │ Envoyer notification à l'ADMIN         │
   │ ✓ Infos complètes du client            │
   │ ✓ Lien direct vers admin panel         │
   │ ✓ Bouton "Répondre"                    │
   └────────────────────────────────────────┘
        ↓
   ┌────────────────────────────────────────┐
   │ Message de succès affiché au CLIENT    │
   │ Redirection vers page contact          │
   └────────────────────────────────────────┘
        ↓
    HISTO EMAILS CONSULTABLE:
    - Admin panel: /admin/produition/message/
    - Infos: sender_email, email_sent, email_sent_at
```

---

## 🛠️ UTILISATION DU SYSTÈME

### 1️⃣ Via le formulaire HTML (dashboard/contact.html)

```html
<form method="POST" action="{% url 'contact' %}">
    {% csrf_token %}
    
    {{ form.sender_name }}
    {{ form.sender_email }}
    {{ form.sender_phone }}
    {{ form.subject }}
    {{ form.message }}
    {{ form.category }}
    
    <button type="submit">Envoyer</button>
</form>
```

### 2️⃣ Via API AJAX (JavaScript)

```javascript
document.getElementById('contactForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(this);
    
    const response = await fetch('/api/send-message/', {
        method: 'POST',
        body: formData
    });
    
    const data = await response.json();
    
    if (data.success) {
        alert('✓ Message envoyé!');
        console.log('Ticket:', data.message_id);
    } else {
        alert('✗ Erreur: ' + data.message);
    }
});
```

---

## 🔍 GESTION ET SUIVI DES MESSAGES

### Admin Panel Django

Accès: `/admin/produition/message/`

**Actions disponibles:**
- Voir tous les messages
- Filtrer par statut (Non lu, Lu, Répondu, Archivé)
- Rechercher par expéditeur/email
- Marquer comme lu
- Modifier le statut
- Voir l'historique d'envoi email

**Colonnes importantes:**
```
| Sender Name | Email | Subject | Category | Status | Email Sent | Date Created |
```

### Requête ORM pour les statistiques

```python
# Tous les messages non lus
Message.objects.filter(status='nouveau')

# Messages sans email confirme
Message.objects.filter(email_sent=False)

# Messages par catégorie
Message.objects.filter(category='devis').count()

# Messages d'aujourd'hui
from django.utils import timezone
today = timezone.now().date()
Message.objects.filter(created_at__date=today)
```

---

## 🚀 DÉPLOIEMENT EN PRODUCTION

### Checklist avant lancement

- [ ] Configurer EMAIL_BACKEND = SMTP
- [ ] Configurer EMAIL_HOST, EMAIL_PORT, etc.
- [ ] Utiliser les identifiants d'app Gmail (Token)
- [ ] Tester l'envoi: `python manage.py shell`

```python
from django.core.mail import send_mail
send_mail(
    'Test',
    'Message de test',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```

- [ ] Vérifier les logs: `/backend/logs/email.log`
- [ ] Configurer ALLOWED_HOSTS
- [ ] Migrer la base de données: `python manage.py migrate`
- [ ] Collecter les fichiers statiques: `python manage.py collectstatic`

---

## 🐛 DÉPANNAGE

### Email non envoyé?

**Vérifier:**
1. `EMAIL_BACKEND` configuré correctement
2. `EMAIL_HOST` et `EMAIL_PORT` corrects
3. Identifiants SMTP valides
4. `DEFAULT_FROM_EMAIL` défini
5. Logs dans `/backend/logs/email.log`

### Erreur "Connection refused"?

```python
# Vérifier le backend dans la console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Puis en production:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```

### Emails marqués comme SPAM?

- Ajouter SPF, DKIM, DMARC records
- Utiliser un domaine valide
- Avoir un contenu HTML propre
- Éviter les liens de phishing

---

## 📞 SUPPORT

Pour toute question sur ce système, consultez:
- Documentation Django: https://docs.djangoproject.com/en/5.2/topics/email/
- EmailMultiAlternatives: https://docs.djangoproject.com/en/5.2/topics/email/#sending-alternative-content-types

---

**Créé pour KINÉRA FILM FIXERS** 🎬
Version: 1.0
Date: 22 Feb 2026
