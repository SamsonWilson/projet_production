# ✅ CHECKLIST - SYSTÈME D'EMAIL KINÉRA

Utilisez cette checklist pour suivre votre progression d'installation.

---

## 📋 PHASE 1: VÉRIFICATION DES FICHIERS

### Fichiers Code
- [ ] `produition/models.py` - Model Message avec 13 champs
- [ ] `produition/Forms/formsContact.py` - Formulaire avec validation
- [ ] `produition/views/views_contact.py` - Vues et envoi email
- [ ] `produition/admin.py` - Configuration admin
- [ ] `produition/urls.py` - Routes
- [ ] `backend/settings.py` - Configuration Django

### Templates Email
- [ ] `templates/emails/message_confirmation.html` - Email client
- [ ] `templates/emails/message_admin_notification.html` - Email admin
- [ ] `templates/dashboard/contact.html` - Formulaire visible

### Documentation
- [ ] `README_EMAIL_SYSTEM.md` - Guide navigation
- [ ] `SYSTEME_EMAIL_GUIDE.md` - Guide technique
- [ ] `SETUP_ETAPES.md` - Installation step-by-step
- [ ] `SUMMARY.md` - Résumé complet
- [ ] `verify_simple.py` - Script vérification
- [ ] `CHECKLIST.md` - Ce fichier

**Status:** ______/16 fichiers ✓

---

## 🔍 PHASE 2: VÉRIFICATION AUTOMATISÉE

### Exécuter le script de vérification

```bash
cd /home/star/Desktop/projet_production/API/backend
python verify_simple.py
```

- [ ] Fichiers Python présents (6/6)
- [ ] Templates Email présents (3/3)
- [ ] Structure dossiers OK (9/9)
- [ ] Contenu vérifiés (7/7)
- [ ] Configuration OK (4/4)
- [ ] Templates variables OK (2/2)

**Résultat attendu:** 31/31 tests (100%) ✓

---

## 🐍 PHASE 3: ENVIRONNEMENT PYTHON

### Configuration

- [ ] Python 3.8+ instalé
- [ ] Virtual environment créé
- [ ] Django installé
- [ ] django-allauth installé
- [ ] mail packages disponibles

**Commande:**
```bash
ls -la /home/star/Desktop/projet_production/API/venv/
```

---

## 💾 PHASE 4: BASE DE DONNÉES

### Migrations

- [ ] `python manage.py makemigrations` exécuté
  - Doit créer: `produition/migrations/0002_message.py`
  
- [ ] `python manage.py migrate` exécuté
  - Doit créer table: `produition_message`

- [ ] Vérifier la table
  ```bash
  python manage.py dbshell
  # SELECT * FROM produition_message;
  ```

**Status:** Migrations ______/2 ✓

---

## 🔧 PHASE 5: CONFIGURATION DJANGO

### settings.py - Email Backend

- [ ] `EMAIL_BACKEND` configuré (console pour dev)
- [ ] `DEFAULT_FROM_EMAIL` défini
- [ ] `ADMIN_EMAIL` défini
- [ ] `LOGGING` configuré

**Vérification:**
```python
# Devrait afficher dans settings.py:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@kinera-filmfixers.com'
ADMIN_EMAIL = 'admin@kinera-filmfixers.com'
```

**Status:** Configuration ______/4 ✓

---

## 👨‍💼 PHASE 6: ADMIN DJANGO

### Enregistrement du modèle

- [ ] `produition/admin.py` modifié
- [ ] `admin.site.register(Message, MessageAdmin)` ajouté
- [ ] `list_display` défini
- [ ] `list_filter` défini
- [ ] `search_fields` défini

**Vérifier:**
```bash
python manage.py runserver
# Aller à: http://localhost:8000/admin/
# Vérifier que "Messages" apparaît dans le menu
```

**Status:** Admin ______/5 ✓

---

## 🔗 PHASE 7: ROUTING URLs

### produition/urls.py

- [ ] `path('contact/', ContactFormView.as_view(), name='contact')` ajouté
- [ ] `path('api/send-message/', send_message_ajax, name='send_message_ajax')` ajouté
- [ ] Imports corrects

**Fichier:**
```python
from produition.views.views_contact import ContactFormView, send_message_ajax

urlpatterns = [
    # ... autres routes ...
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('api/send-message/', send_message_ajax, name='send_message_ajax'),
]
```

**Status:** URLs ______/3 ✓

---

## 🌐 PHASE 8: INTERFACE WEB

### Tester le formulaire en développement

```bash
python manage.py runserver
```

**Tests à faire:**
- [ ] Aller à `http://localhost:8000/contact/`
- [ ] Formulaire s'affiche correctement
- [ ] Le styling Bootstrap s'applique
- [ ] Remplir correctement le formulaire

**Test d'ERREURS:**
- [ ] Nom trop court: affiche erreur ✓
- [ ] Email invalide: affiche erreur ✓
- [ ] Message trop court: affiche erreur ✓
- [ ] Tous champs vides: affiche erreurs ✓

**Status:** Interface ______/8 ✓

---

## 📧 PHASE 9: TESTER L'ENVOI D'EMAIL (DEV)

### En mode console

**Remplir le formulaire et envoyer:**

- [ ] Formulaire dit "Message envoyé avec succès"
- [ ] Console Django affiche l'email du CLIENT
- [ ] Console Django affiche l'email de l'ADMIN
- [ ] Les 2 emails ont le contenu HTML

**Exemple de sortie attendue:**
```
From: noreply@kinera-filmfixers.com
To: jean@example.com
Subject: Confirmation de votre message - KINÉRA
[Email avec HTML...]

---

From: noreply@kinera-filmfixers.com
To: admin@kinera-filmfixers.com
Subject: Nouveau message reçu
[Email avec HTML...]
```

**Status:** Emails Envoyés ______/4 ✓

---

## 📊 PHASE 10: VÉRIFIER LA BASE DE DONNÉES

### Message sauvegardé correctement

```bash
python manage.py shell

from produition.models import Message

# Voir le message créé
msg = Message.objects.last()
print(f"ID: {msg.id}")
print(f"From: {msg.sender_name} ({msg.sender_email})")
print(f"Subject: {msg.subject}")
print(f"Status: {msg.status}")
print(f"Email sent: {msg.email_sent}")
print(f"Email sent at: {msg.email_sent_at}")
```

- [ ] Message créé avec ID unique
- [ ] Tous les champs remplis correctement
- [ ] `email_sent = True`
- [ ] `email_sent_at` = datetime
- [ ] `status = 'nouveau'`

**Status:** Database ______/5 ✓

---

## 🎯 PHASE 11: ADMIN PANEL

### Gérer les messages via l'admin

```bash
# Aller à: http://localhost:8000/admin/produition/message/
```

- [ ] Message apparaît dans la liste
- [ ] Affiche: sender_name, email, subject, status, email_sent
- [ ] Peut cliquer pour voir détails
- [ ] Peut changer le statut
- [ ] Peut filtrer par status/category

**Colonnes visibles:**
- sender_name: ______
- sender_email: ______
- subject: ______
- status: ______
- email_sent: ______
- created_at: ______

**Status:** Admin Message ______/6 ✓

---

## 🧪 PHASE 12: TESTS SUPPLÉMENTAIRES

### Validation du formulaire

- [ ] Tester avec données valides → Message reçu ✓
- [ ] Tester avec email invalide → Erreur affichée ✓
- [ ] Tester avec message court → Erreur affichée ✓
- [ ] Tester avec tous champs vides → Erreurs multiples ✓
- [ ] Tester caractères spéciaux → Acceptés correctement ✓

### Tests de performance

- [ ] Page contact charge < 2s
- [ ] Admin panel charges < 3s
- [ ] Email s'envoie sans délai
- [ ] Aucune erreur 500

**Status:** Tests ______/8 ✓

---

## 🚀 PHASE 13: PRÉPARATION PRODUCTION

### Avant déploiement

- [ ] DEBUG = False dans settings.py
- [ ] ALLOWED_HOSTS configuré
- [ ] Email backend changé de CONSOLE à SMTP

### Configuration SMTP Gmail

- [ ] Compte Gmail préparé
- [ ] App password généré
- [ ] EMAIL_HOST = 'smtp.gmail.com'
- [ ] EMAIL_PORT = 587
- [ ] EMAIL_HOST_USER = votre-email@gmail.com
- [ ] EMAIL_HOST_PASSWORD = app-password

**Générer app password:**
1. Aller: https://myaccount.google.com/apppasswords
2. Sélectionner: Mail + Linux
3. Copier le password 16-caractères
4. Coller dans EMAIL_HOST_PASSWORD

**Status:** Production Setup ______/6 ✓

---

## ✅ PHASE 14: TEST PRODUCTION

### Avant de lancer

```bash
python manage.py shell

from django.core.mail import send_mail

send_mail(
    'Test Email Production',
    'Ceci est un test d\'email depuis la production',
    'contact@kinera.com',
    ['admin@kinera.com'],
    fail_silently=False,
)
```

- [ ] Email s'envoie sans erreur
- [ ] Email reçu dans la boîte
- [ ] Contenu HTML correct
- [ ] Pas dans SPAM

### Vérifier les logs

- [ ] Voir `logs/email.log`
- [ ] Affiche les succès d'envoi
- [ ] Affiche les erreurs (s'il y en a)

**Status:** Production Test ______/6 ✓

---

## 📱 PHASE 15: TESTS MOBILE

### Responsive Design

- [ ] Formulaire s'affiche bien sur mobile
- [ ] Email confirmation responsive sur mobile
- [ ] Email admin responsive sur mobile
- [ ] Boutons cliquables sur petit écran

**Tester sur:**
- [ ] iPhone (375px)
- [ ] Android (360px)
- [ ] Tablette (768px)

**Status:** Mobile ______/7 ✓

---

## 🔐 PHASE 16: SÉCURITÉ

### Avant production

- [ ] CSRF token dans le formulaire
- [ ] EmailValidator sur email field
- [ ] Longueur minimale/maximale respectée
- [ ] Pas de SQL injection possible
- [ ] Rate limiting (à faire)
- [ ] reCAPTCHA (à faire - optionnel)

**Status:** Sécurité ______/6 ✓

---

## 📚 PHASE 17: DOCUMENTATION

### Finalisée

- [ ] README_EMAIL_SYSTEM.md complet
- [ ] SYSTEME_EMAIL_GUIDE.md détaillé
- [ ] SETUP_ETAPES.md clair
- [ ] SUMMARY.md à jour
- [ ] CHECKLIST.md complète
- [ ] Code commenté

**Status:** Documentation ______/6 ✓

---

## 🎉 STATUT FINAL

### Résumé de l'installation

| Phase | Nom | Status | Progress |
|-------|-----|--------|----------|
| 1 | Fichiers | ______/3 | ___ % |
| 2 | Vérification | 31/31 ✓ | 100% |
| 3 | Python | ______/5 | ___ % |
| 4 | Database | ______/2 | ___ % |
| 5 | Configuration | ______/4 | ___ % |
| 6 | Admin | ______/5 | ___ % |
| 7 | URLs | ______/3 | ___ % |
| 8 | Interface | ______/8 | ___ % |
| 9 | Emails Dev | ______/4 | ___ % |
| 10 | Database Check | ______/5 | ___ % |
| 11 | Admin Panel | ______/6 | ___ % |
| 12 | Tests | ______/8 | ___ % |
| 13 | Production Setup | ______/6 | ___ % |
| 14 | Production Test | ______/6 | ___ % |
| 15 | Mobile | ______/7 | ___ % |
| 16 | Sécurité | ______/6 | ___ % |
| 17 | Documentation | ______/6 | ___ % |

**TOTAL:** ______/125 points

---

## 🎯 OBJECTIF FINAL

**Quand toutes les cases sont cochées ✓:**

- ✅ Système d'email complètement fonctionnel
- ✅ Prêt pour production
- ✅ Bien documenté
- ✅ Sécurisé
- ✅ Responsive
- ✅ Testé

---

## 💡 TIPS

### Pour mieux suivre:
1. **Imprimer cette checklist** et cocher à mesure
2. **Suivre l'ordre** des phases (très important!)
3. **Tester après chaque étape** pour trouver erreurs rapidement
4. **Consulter la documentation** si problème

### Où trouver de l'aide:
- SETUP_ETAPES.md → Pour installation
- SYSTEME_EMAIL_GUIDE.md → Pour comprendre
- SUMMARY.md → Pour vue globale
- README_EMAIL_SYSTEM.md → Pour nav rapide

---

**Créé pour KINÉRA FILM FIXERS** 🎬

**Version:** 1.0  
**Date:** 22 Feb 2026

**Bonne installation!** 🚀
