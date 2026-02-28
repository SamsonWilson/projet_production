# ✅ GUIDE DE SETUP - ÉTAPES D'INSTALLATION

## 📋 PRÉREQUIS

- Django 5.2.7 installé ✓
- Python 3.8+ ✓
- Base de données configurée ✓
- Dossier `/logs` créé dans `/backend/` ✓

---

## 🔧 ÉTAPES D'INSTALLATION - À EXÉCUTER DANS L'ORDRE

### ÉTAPE 1: Créer les migrations de la base de données

**Commande:**
```bash
cd /home/star/Desktop/projet_production/API/backend
python manage.py makemigrations
```

**Sortie attendue:**
```
Migrations for 'produition':
  produition/migrations/0002_message.py
    - Create model Message
```

**Vérification:**
```bash
# Voir les migrations en attente
python manage.py showmigrations produition
```

---

### ÉTAPE 2: Appliquer les migrations

**Commande:**
```bash
python manage.py migrate
```

**Sortie attendue:**
```
Running migrations:
  Applying produition.0002_message... OK
```

**Vérification:**
```bash
# Voir la table créée
python manage.py dbshell
# Puis: SELECT * FROM produition_message;
# (devrait être vide pour l'instant)
```

---

### ÉTAPE 3: Enregistrer le modèle dans l'admin Django

**Fichier:** `produition/admin.py`

```python
from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_email', 'subject', 'category', 'status', 'email_sent', 'created_at')
    list_filter = ('status', 'category', 'email_sent', 'created_at')
    search_fields = ('sender_name', 'sender_email', 'subject')
    readonly_fields = ('email_sent', 'email_sent_at', 'created_at', 'updated_at', 'read_at')
    fieldsets = (
        ('Infos Expéditeur', {
            'fields': ('sender_name', 'sender_email', 'sender_phone')
        }),
        ('Contenu', {
            'fields': ('subject', 'message', 'category')
        }),
        ('Statut', {
            'fields': ('status', 'read_at')
        }),
        ('Email', {
            'fields': ('email_sent', 'email_sent_at'),
            'classes': ('collapse',)
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Message, MessageAdmin)
```

---

### ÉTAPE 4: Mettre à jour les URLs

**Fichier:** `produition/urls.py`

```python
from django.urls import path
from .views.views_contact import ContactFormView, send_message_ajax

urlpatterns = [
    # Route existantes...
    
    # Ajouter ces 2 lignes:
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('api/send-message/', send_message_ajax, name='send_message_ajax'),
]
```

---

### ÉTAPE 5: Vérifier la configuration email (settings.py)

**Pour le DÉVELOPPEMENT** (Affiche les emails dans la console):
```python
# Déjà configuré par défaut
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@kinera-filmfixers.com'
ADMIN_EMAIL = 'admin@kinera-filmfixers.com'
```

**Pour la PRODUCTION** (Exemple Gmail):
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre-email@gmail.com'
EMAIL_HOST_PASSWORD = 'app-password'  # Généré via Google Account
DEFAULT_FROM_EMAIL = 'contact@kinera-filmfixers.com'
ADMINS = [('Admin', 'admin@kinera-filmfixers.com')]
ADMIN_EMAIL = 'admin@kinera-filmfixers.com'
```

---

### ÉTAPE 6: Mettre à jour le formulaire contact (optionnel)

**Fichier:** `dashboard/contact.html`

Si vous avez un formulaire de contact existant, mettez-à-jour l'action:

```html
<form method="POST" action="{% url 'contact' %}" id="contactForm">
    {% csrf_token %}
    
    <div class="form-group">
        <label for="id_sender_name">Nom:</label>
        {{ form.sender_name }}
        {% if form.sender_name.errors %}
            <div class="error">{{ form.sender_name.errors }}</div>
        {% endif %}
    </div>
    
    <div class="form-group">
        <label for="id_sender_email">Email:</label>
        {{ form.sender_email }}
        {% if form.sender_email.errors %}
            <div class="error">{{ form.sender_email.errors }}</div>
        {% endif %}
    </div>
    
    <div class="form-group">
        <label for="id_sender_phone">Téléphone (optionnel):</label>
        {{ form.sender_phone }}
    </div>
    
    <div class="form-group">
        <label for="id_subject">Sujet:</label>
        {{ form.subject }}
        {% if form.subject.errors %}
            <div class="error">{{ form.subject.errors }}</div>
        {% endif %}
    </div>
    
    <div class="form-group">
        <label for="id_message">Message:</label>
        {{ form.message }}
        {% if form.message.errors %}
            <div class="error">{{ form.message.errors }}</div>
        {% endif %}
    </div>
    
    <div class="form-group">
        <label for="id_category">Catégorie:</label>
        {{ form.category }}
    </div>
    
    <button type="submit" class="btn btn-primary">Envoyer</button>
</form>
```

---

## ✅ TEST DU SYSTÈME

### Test 1: Test direct en Python

```bash
cd /home/star/Desktop/projet_production/API/backend
python manage.py shell
```

```python
# Importer le modèle
from produition.models import Message
from django.utils import timezone

# Créer un message de test
test_message = Message.objects.create(
    sender_name="Jean Dupont",
    sender_email="jean@example.com",
    sender_phone="+33612345678",
    subject="Demande de devis test",
    message="Ceci est un message de test pour vérifier le système.",
    category="devis",
    status="nouveau"
)

# Vérifier que c'est créé
print(f"Message créé: ID={test_message.id}")

# Tester l'envoi d'email
from produition.views.views_contact import send_email_to_sender, send_email_to_admin
from django.test import RequestFactory

factory = RequestFactory()
request = factory.post('/contact/')

# Envoyer les emails
sender_result = send_email_to_sender(test_message, request)
admin_result = send_email_to_admin(test_message, request)

print(f"Email client envoyé: {sender_result}")
print(f"Email admin envoyé: {admin_result}")
```

### Test 2: Test via le formulaire HTML

1. Aller à: `http://localhost:8000/contact/`
2. Remplir le formulaire
3. Cliquer "Envoyer"
4. Vérifier les emails dans la console Django (mode dev)

### Test 3: Vérifier la base de données

```bash
python manage.py dbshell
```

```sql
-- Voir tous les messages
SELECT id, sender_name, sender_email, subject, status, email_sent, created_at 
FROM produition_message;

-- Voir les messages non lus
SELECT * FROM produition_message WHERE status = 'nouveau';

-- Voir les messages sans email confirmé
SELECT * FROM produition_message WHERE email_sent = 0;
```

---

## 🚀 DÉMARRER LE SERVEUR

```bash
cd /home/star/Desktop/projet_production/API/backend

# Version simple
python manage.py runserver

# Version avec port spécifique
python manage.py runserver 0.0.0.0:8000

# Avec rechargement auto
python manage.py runserver --reload
```

**Accès:**
- Site: http://localhost:8000/
- Admin panel: http://localhost:8000/admin/
- Messages: http://localhost:8000/admin/produition/message/

---

## 📧 CONSOLE DE DÉVELOPPEMENT

En mode développement, les emails s'affichent dans la console du serveur Django:

```
[Email backend: console EmailBackend]

From: noreply@kinera-filmfixers.com
To: jean@example.com
Subject: Confirmation de votre message - KINÉRA

Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit

Bonjour Jean,

Votre message a bien été reçu...

---

[Next email]
From: noreply@kinera-filmfixers.com
To: admin@kinera-filmfixers.com
Subject: Nouveau message reçu

...
```

---

## 🔍 VÉRIFIER LES LOGS

```bash
# Voir les logs des emails
tail -f /home/star/Desktop/projet_production/API/backend/logs/email.log

# Voir les erreurs
grep ERROR /home/star/Desktop/projet_production/API/backend/logs/email.log

# Voir tous les envois
grep "Email sent" /home/star/Desktop/projet_production/API/backend/logs/email.log
```

---

## 📱 ADMIN PANEL - GESTION DES MESSAGES

**URL:** http://localhost:8000/admin/produition/message/

**Actions:**
1. **Voir les messages:** Affiche tous les messages reçus
2. **Filtrer:** Par statut, catégorie, date
3. **Rechercher:** Par nom expéditeur, email, sujet
4. **Modifier:** Changer le statut, marquer comme lu
5. **Supprimer:** Nettoyer les anciens messages (attention!)

---

## 🐛 TROUBLESHOOTING

### Problème: "ModuleNotFoundError: No module named 'produce'"

**Solution:**
```bash
# Vérifier le chemin Python
python -c "import sys; print(sys.path)"

# Ajouter le chemin du projet
export PYTHONPATH="/home/star/Desktop/projet_production/API/backend:$PYTHONPATH"

# Relancer Django
python manage.py runserver
```

### Problème: "No such table: produition_message"

**Solution:**
```bash
# Refaire les migrations
python manage.py makemigrations
python manage.py migrate

# Vérifier
python manage.py showmigrations
```

### Problème: "email_sent" column doesn't exist

**Solution:**
```bash
# Votre ancienne migration n'a pas les nouveaux champs
# Supprimer et refaire:
python manage.py migrate produition 0001_initial
python manage.py migrate  # Pour réappliquer les migrations
```

### Problème: Les emails ne s'envoient pas en production

**Vérifications:**
1. ✅ Configurer EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
2. ✅ Configurer DEFAULT_FROM_EMAIL (doit être un domaine valide)
3. ✅ DEBUG = False dans settings.py
4. ✅ Vérifier les logs: `/backend/logs/email.log`
5. ✅ Tester avec: `python manage.py shell` → `send_mail(...)`

---

## 📊 STATISTIQUES

Pour suivre les messages:

```python
# Dans Django shell
from produition.models import Message
from django.utils import timezone

# Nombre total
Message.objects.count()

# Par catégorie
Message.objects.values('category').annotate(count=Count('id'))

# Non lus
Message.objects.filter(status='nouveau').count()

# Emails envoyés aujourd'hui
from datetime import timedelta
today = timezone.now().date()
Message.objects.filter(email_sent_at__date=today).count()

# Taux de réussite email
total = Message.objects.count()
success = Message.objects.filter(email_sent=True).count()
print(f"Taux de succès: {success}/{total} = {success/total*100:.1f}%")
```

---

## ✨ PROCHAINES ÉTAPES (OPTIONNEL)

1. **Créer une page d'admin personnalisée** pour voir les stats des messages
2. **Ajouter des notifications en temps réel** (WebSocket)
3. **Implémenter un système de réponse automatique** pour certaines catégories
4. **Créer des rapports mensuels** PDF avec statistiques
5. **Ajouter reCAPTCHA** pour éviter le spam

---

**Créé pour KINÉRA FILM FIXERS** 🎬
Version: 1.0
Date: 22 Feb 2026
