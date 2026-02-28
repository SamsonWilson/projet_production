# 📧 SYSTÈME D'EMAIL - DOCUMENTATION COMPLÈTE

Bienvenue dans la documentation du **système d'envoi de messages avec emails automatiques** pour KINÉRA FILM FIXERS.

---

## 📚 FICHIERS DE DOCUMENTATION

Voici tous les fichiers créés pour vous aider :

### 1. **README.md** (Ce fichier)
- Guide de navigation
- Vue d'ensemble rapide
- Où trouver quoi

### 2. **SYSTEME_EMAIL_GUIDE.md** (DETAILED GUIDE)
**Pour comprendre en détail comment tout fonctionne**

Contient:
- 📋 Architecture du système
- 🔧 Détails techniques de chaque composant
- 📤 Flux complet d'un message
- 🛠️ Utilisation du système
- 🔍 Gestion des messages en admin
- 🚀 Déploiement en production

**Lire si:** Vous voulez comprendre en profondeur comment fonctionne le système

### 3. **SETUP_ETAPES.md** (INSTALLATION GUIDE)
**Pour installer et mettre en marche le système**

Contient:
- ✅ Étapes d'installation (1-6)
- ✅ Tests du système
- 🚀 Démarrer le serveur
- 📧 Console de développement
- 📊 Accéder à l'admin panel
- 🐛 Troubleshooting

**Lire si:** Vous configurez le système pour la première fois

### 4. **verify_email_system.py** (SCRIPT DE VÉRIFICATION)
**Vérifier automatiquement que tout est configuré correctement**

Exécuter avec:
```bash
python verify_email_system.py
```

Vérifie:
- ✓ Configuration Django
- ✓ Modèles (Message model)
- ✓ Fichiers (Tous les fichiers nécessaires)
- ✓ Base de données (Table Message)
- ✓ Email configuration
- ✓ Validation du formulaire

**À faire:** Après chaque installation/modification

---

## 🎯 DÉMARRAGE RAPIDE (5 MIN)

### Étape 1: Cloner et installer
```bash
cd /home/star/Desktop/projet_production/API/backend
pip install -r requirements.txt
```

### Étape 2: Vérifier la configuration
```bash
python verify_email_system.py
```
→ Doit afficher **100% SUCCÈS** ✓

### Étape 3: Créer la table en base de données
```bash
python manage.py makemigrations
python manage.py migrate
```

### Étape 4: Démarrer le serveur
```bash
python manage.py runserver
```

### Étape 5: Tester
1. Aller à: http://localhost:8000/contact/
2. Remplir le formulaire
3. Envoyer
4. Voir l'email dans la **console Django** ← Il s'y affiche parce qu'on est en développement
5. Vérifier en base: http://localhost:8000/admin/produition/message/

---

## 📍 OÙ TROUVER LES FICHIERS

### Code Python
```
API/backend/
├── produition/
│   ├── models.py                 # Modèle Message
│   ├── Forms/
│   │   └── formsContact.py       # Validation formulaire
│   ├── views/
│   │   └── views_contact.py      # Envoi emails
│   └── urls.py                   # Routes
├── backend/
│   └── settings.py               # Configuration email
```

### Templates HTML
```
templates/
├── dashboard/
│   └── contact.html              # Formulaire visible
└── emails/
    ├── message_confirmation.html      # Email client
    └── message_admin_notification.html # Email admin
```

### Documentation
```
API/backend/
├── README.md                     # Ce fichier
├── SYSTEME_EMAIL_GUIDE.md        # Guide détaillé
├── SETUP_ETAPES.md               # Étapes installation
└── verify_email_system.py        # Script vérification
```

---

## 🔄 FLUX DU SYSTÈME (VISUEL)

```
┌─────────────────────────────────────────────────┐
│  UTILISATEUR REMPLIT LE FORMULAIRE CONTACT      │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│  VALIDATION PAR MessageForm                     │
│  - 2-100 caractères pour le nom                │
│  - Email valide                                 │
│  - 10-5000 caractères pour le message          │
└─────────────────────────────────────────────────┘
            ↓ (valide)      ↓ (erreur)
            │               └─→ Afficher form + erreurs
            ↓
┌─────────────────────────────────────────────────┐
│  SAUVEGARDER EN BASE DE DONNÉES                 │
│  Message object créé avec ID unique             │
└─────────────────────────────────────────────────┘
                      ↓
        ┌─────────────┴─────────────┐
        ↓                           ↓
   ┌─────────────┐          ┌──────────────┐
   │  EMAIL AU   │          │  EMAIL À     │
   │  CLIENT     │          │  L'ADMIN     │
   └─────────────┘          └──────────────┘
        ↓                           ↓
   message_                  message_admin_
   confirmation.html         notification.html
        ↓                           ↓
   - Greeting                  - Infos sender
   - Récapitulatif             - Catégorie
   - N° ticket                 - Full message
   - CTA Bouton                - Links action
        ↓                           ↓
┌─────────────────────────────────────────────────┐
│  ENVOYER VIA settings.EMAIL_BACKEND             │
│  - Console (dev): affiche dans terminal         │
│  - SMTP (prod): envoie par email                │
└─────────────────────────────────────────────────┘
        ↓ (succès)         ↓ (erreur)
        │                  └→ Logger erreur
        ↓
┌─────────────────────────────────────────────────┐
│  MARQUER COMME ENVOYÉ                           │
│  message.email_sent = True                      │
│  message.email_sent_at = now()                  │
└─────────────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────────┐
│  AFFICHER SUCCÈS À L'UTILISATEUR                │
│  "Message envoyé avec succès"                   │
└─────────────────────────────────────────────────┘
```

---

## 📧 CONFIGURATION EMAIL

### Pour DÉVELOPPEMENT (Console)
✓ Déjà configuré par défaut
- Les emails s'affichent dans la console Django
- Parfait pour tester localement
- NE crée PAS de vrais emails

```python
# Dans settings.py (déjà fait)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### Pour PRODUCTION (Gmail)
À faire avant de déployer:

```python
# Dans settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre-email@gmail.com'
EMAIL_HOST_PASSWORD = 'app-password-generee-par-google'
```

📍 Comment obtenir une "app password" Gmail:
1. Aller: https://myaccount.google.com/apppasswords
2. Générer un mot de passe pour "Mail"
3. Copier le mot de passe dans EMAIL_HOST_PASSWORD

### Pour AUTRES SERVEURS (SendGrid, Mailgun, etc.)
Voir **SYSTEME_EMAIL_GUIDE.md** → "CONFIGURATION DJANGO"

---

## 🧪 TESTER LE SYSTÈME

### Test 1: Vérification rapide
```bash
python verify_email_system.py
```
La meilleure façon de tester rapidement

### Test 2: Mode interactif
```bash
python manage.py shell
```

```python
from produition.models import Message

# Créer un message de test
msg = Message.objects.create(
    sender_name="Test",
    sender_email="test@example.com",
    subject="Message de test",
    message="Ceci est un message de test"
)

# Vérifier
print(f"Message créé: ID={msg.id}, Email sent: {msg.email_sent}")

# Voir les emails dans la console
from produition.views.views_contact import send_email_to_sender
from django.test import RequestFactory

factory = RequestFactory()
request = factory.post('/contact/')
send_email_to_sender(msg, request)
```

### Test 3: Via le formulaire
1. Démarrer: `python manage.py runserver`
2. Aller: http://localhost:8000/contact/
3. Remplir et envoyer
4. Voir l'email dans la **console Django**

---

## 🔍 COMPRENDRE LES COMPOSANTS

### Message Model (Database)
**Fichier:** `produition/models.py`

La table qui stocke tous les messages:

```
Champs principaux:
├── sender_name        → Qui envoie?
├── sender_email       → Email du client
├── subject            → Sujet du message
├── message            → Contenu
├── category           → Type (devis, reclamation, etc.)
├── status             → État (nouveau, lu, repondu...)
├── email_sent         → Confirmation email envoyé?
├── created_at         → Quand créé?
└── updated_at         → Dernière modification?
```

### MessageForm (Validation)
**Fichier:** `produition/Forms/formsContact.py`

Valide les données avant de sauvegarder:
- Nom: 2-100 caractères
- Email: Format valide
- Subject: 5-200 caractères
- Message: 10-5000 caractères
- Catégorie: Choix prédéfinis

### ContactFormView (Vue)
**Fichier:** `produition/views/views_contact.py`

Gère le formulaire:
1. `GET /contact/` → Afficher le formulaire
2. `POST /contact/` → Recevoir les données
3. Valider avec MessageForm
4. Sauvegarder en base
5. Envoyer 2 emails
6. Afficher succès

### Email Templates (UI)
**Fichier:** `templates/emails/`

**message_confirmation.html** → Reçu par le CLIENT
- Message de confirmation
- N° de ticket unique
- Info de suivi

**message_admin_notification.html** → Reçu par l'ADMIN
- Détails du sender
- Lien pour répondre
- Alerte spéciale si urgent

---

## 🚀 DÉPLOIEMENT EN PRODUCTION

### Checklist
```
✓ Changer EMAIL_BACKEND de console à SMTP
✓ Configurer EMAIL_HOST, EMAIL_PORT, etc.
✓ Utiliser app-password Gmail ou SMTP valide
✓ DEBUG = False dans settings.py
✓ Mettre à jour ALLOWED_HOSTS
✓ Exécuter: python manage.py migrate
✓ Tester sends_mail() depuis shell
✓ Vérifier les logs: logs/email.log
✓ Générer static files: python manage.py collectstatic
✓ Configurer le serveur (Gunicorn/Apache)
```

### Tester avant production
```bash
python manage.py shell

from django.core.mail import send_mail

send_mail(
    'Test Production',
    'Ceci est un test',
    'contact@kinera.com',
    ['admin@kinera.com'],
    fail_silently=False,
)
```

---

## 🐛 PROBLÈMES COURANTS

### Les emails ne s'affichent pas
→ Vérifiez que `EMAIL_BACKEND = 'console.EmailBackend'` (console pour dev)

### Erreur "Table doesn't exist"
→ Exécutez: `python manage.py makemigrations && python manage.py migrate`

### Les emails ne s'envoient pas en production
→ Vérifiez EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

### Emails dans SPAM
→ Configurez SPF, DKIM, DMARC sur votre domaine

Pour plus: Voir **SETUP_ETAPES.md** → "TROUBLESHOOTING"

---

## 📞 RESSOURCES

- **Django Mail Documentation**: https://docs.djangoproject.com/en/5.2/topics/email/
- **EmailMultiAlternatives**: https://docs.djangoproject.com/en/5.2/topics/email/#sending-alternative-content-types
- **Gmail App Passwords**: https://myaccount.google.com/apppasswords
- **SMTP Ports**: https://en.wikipedia.org/wiki/SMTP

---

## 📊 STATISTIQUES DU SYSTÈME

```
✓ Fichiers créés:             7
✓ Lignes de code:             ~2000
✓ Templates email:            2
✓ Champs validés:             6
✓ Catégories supportées:      4 (devis, reclamation, general, partenariat)
✓ Statuts de message:         4 (nouveau, lu, repondu, archive)
✓ Emails envoyés:             2 par message (client + admin)
✓ Support des formats:        HTML + Texte
```

---

## ✨ PROCHAINES ÉTAPES

1. **Lire SETUP_ETAPES.md** pour installer le système
2. **Exécuter verify_email_system.py** pour vérifier
3. **Tester avec un formulaire** en développement
4. **Configurer SMTP** pour la production
5. **Lancer en production**

---

## 📝 NOTES

- Tous les emails sont templates Django (HTML + texte)
- Utilisation de `EmailMultiAlternatives` pour support HTML/texte
- Logs sauvegardés dans `/backend/logs/email.log`
- Status de production hérité par la base de données
- Admin panel intégré pour gérer les messages
- Système prêt pour décentralisation (WebHooks, Queues, etc.)

---

**Créé pour KINÉRA FILM FIXERS** 🎬
Version: 1.0
Dernière mise à jour: 22 Feb 2026

**Questions?** Consultez la documentation appropriée ci-dessus!
