#!/usr/bin/env python
"""
VÉRIFICATION SIMPLE - SYSTÈME D'EMAIL KINÉRA
Version simplifiée qui ne nécessite pas django.setup()
"""

import os
import sys
from pathlib import Path

# Configuration des couleurs
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def check(condition, message):
    """Affiche le résultat d'une vérification."""
    if condition:
        print(f"{Colors.GREEN}✓{Colors.ENDC} {message}")
        return True
    else:
        print(f"{Colors.RED}✗{Colors.ENDC} {message}")
        return False

def header(title):
    """Affiche un titre."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.BLUE}{title.center(60)}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.ENDC}\n")

results = []

print(f"\n{Colors.BOLD}{Colors.BLUE}")
print("╔════════════════════════════════════════════════════════════╗")
print("║  VÉRIFICATION SIMPLE - SYSTÈME D'EMAIL KINÉRA             ║")
print("╚════════════════════════════════════════════════════════════╝")
print(f"{Colors.ENDC}\n")

# ========== Vérification 1: Fichiers Python ==========
header("1. FICHIERS PYTHON")

backend_path = Path(__file__).parent

files = {
    'produition/models.py': 'Modèle Message',
    'produition/Forms/formsContact.py': 'Formulaire Contact',
    'produition/views/views_contact.py': 'Vues Contact',
    'produition/admin.py': 'Admin configuration',
    'produition/urls.py': 'URLs',
    'backend/settings.py': 'Paramètres Django',
}

for filepath, desc in files.items():
    full = backend_path / filepath
    exists = full.exists()
    check(exists, f"{desc:30} {filepath}")
    results.append(exists)

# ========== Vérification 2: Templates Email ==========
header("2. TEMPLATES EMAIL")

templates = {
    'templates/emails/message_confirmation.html': 'Email client',
    'templates/emails/message_admin_notification.html': 'Email admin',
    'templates/dashboard/contact.html': 'Page contact',
}

for template, desc in templates.items():
    full = backend_path / template
    exists = full.exists()
    check(exists, f"{desc:30} {template}")
    results.append(exists)

# ========== Vérification 3: Structure des Dossiers ==========
header("3. STRUCTURE DES DOSSIERS")

dirs = {
    'produition': 'App Production',
    'produition/Forms': 'Dossier Forms',
    'produition/views': 'Dossier Views',
    'produition/migrations': 'Migrations',
    'templates': 'Templates',
    'templates/emails': 'Templates Emails',
    'templates/dashboard': 'Templates Dashboard',
    'templates/Admin': 'Templates Admin',
    'logs': 'Logs directory',
}

for dirname, desc in dirs.items():
    full = backend_path / dirname
    exists = full.is_dir()
    check(exists, f"{desc:30} {dirname}/")
    results.append(exists)

# ========== Vérification 4: Contenu des Fichiers ==========
header("4. VÉRIFICATION DU CONTENU")

# Vérifier Message model
try:
    with open(backend_path / 'produition/models.py') as f:
        content = f.read()
    has_message_model = 'class Message' in content
    check(has_message_model, "Modèle Message défini")
    results.append(has_message_model)
    
    has_email_sent = 'email_sent' in content
    check(has_email_sent, "Champ 'email_sent' présent")
    results.append(has_email_sent)
except Exception as e:
    check(False, f"Erreur dans models.py: {e}")
    results.append(False)

# Vérifier MessageForm
try:
    with open(backend_path / 'produition/Forms/formsContact.py') as f:
        content = f.read()
    has_form = 'class MessageForm' in content
    check(has_form, "MessageForm défini")
    results.append(has_form)
    
    has_validation = 'clean_' in content
    check(has_validation, "Méthodes de validation présentes")
    results.append(has_validation)
except Exception as e:
    check(False, f"Erreur dans formsContact.py: {e}")
    results.append(False)

# Vérifier Views
try:
    with open(backend_path / 'produition/views/views_contact.py') as f:
        content = f.read()
    has_send_email = 'def send_email_' in content
    check(has_send_email, "Fonctions d'envoi email")
    results.append(has_send_email)
    
    has_contact_view = 'class ContactFormView' in content
    check(has_contact_view, "ContactFormView définie")
    results.append(has_contact_view)
    
    has_ajax = 'def send_message_ajax' in content
    check(has_ajax, "Endpoint AJAX présent")
    results.append(has_ajax)
except Exception as e:
    check(False, f"Erreur dans views_contact.py: {e}")
    results.append(False)

# ========== Vérification 5: Configuration Settings ==========
header("5. CONFIGURATION DJANGO")

try:
    with open(backend_path / 'backend/settings.py') as f:
        content = f.read()
    
    has_email_backend = 'EMAIL_BACKEND' in content
    check(has_email_backend, "EMAIL_BACKEND configuré")
    results.append(has_email_backend)
    
    has_default_from = 'DEFAULT_FROM_EMAIL' in content
    check(has_default_from, "DEFAULT_FROM_EMAIL configuré")
    results.append(has_default_from)
    
    has_admin_email = 'ADMIN_EMAIL' in content or 'ADMINS' in content
    check(has_admin_email, "Email admin configuré")
    results.append(has_admin_email)
    
    has_logging = 'LOGGING' in content
    check(has_logging, "Logging configuré")
    results.append(has_logging)
except Exception as e:
    check(False, f"Erreur dans settings.py: {e}")
    results.append(False)

# ========== Vérification 6: Templates Email Content ==========
header("6. CONTENU DES TEMPLATES EMAIL")

try:
    with open(backend_path / 'templates/emails/message_confirmation.html') as f:
        content = f.read()
    has_content = 'sender_name' in content and 'message_id' in content
    check(has_content, "Template confirmation a le contexte")
    results.append(has_content)
except Exception as e:
    check(False, f"Erreur template confirmation: {e}")
    results.append(False)

try:
    with open(backend_path / 'templates/emails/message_admin_notification.html') as f:
        content = f.read()
    has_content = 'sender_email' in content and 'category' in content
    check(has_content, "Template admin a le contexte")
    results.append(has_content)
except Exception as e:
    check(False, f"Erreur template admin: {e}")
    results.append(False)

# ========== RÉSUMÉ ==========
header("RÉSUMÉ")

total = len(results)
passed = sum(results)
percentage = (passed / total * 100) if total > 0 else 0

print(f"{Colors.BOLD}Total de vérifications: {passed}/{total} ({percentage:.1f}%){Colors.ENDC}\n")

if percentage == 100:
    print(f"{Colors.GREEN}{Colors.BOLD}✓ TOUS LES TESTS RÉUSSIS! {percentage:.0f}%{Colors.ENDC}")
    print(f"{Colors.GREEN}Votre système d'email est complet et prêt!{Colors.ENDC}\n")
    
    print(f"{Colors.BLUE}PROCHAINES ÉTAPES:{Colors.ENDC}")
    print(f"1. Configurer l'environnement Python")
    print(f"2. Exécuter: python manage.py makemigrations")
    print(f"3. Exécuter: python manage.py migrate")
    print(f"4. Exécuter: python manage.py runserver")
    print(f"5. Visiter: http://localhost:8000/contact/\n")
    
elif percentage >= 75:
    print(f"{Colors.YELLOW}{Colors.BOLD}⚠ PLUPART DES FICHIERS SONT PRÉSENTS {percentage:.0f}%{Colors.ENDC}")
    print(f"{Colors.YELLOW}Quelques fichiers manquent.{Colors.ENDC}\n")
    
else:
    print(f"{Colors.RED}{Colors.BOLD}✗ PLUSIEURS FICHIERS MANQUENT {percentage:.0f}%{Colors.ENDC}")
    print(f"{Colors.RED}Assurez-vous que tous les fichiers ont été créés.{Colors.ENDC}\n")

# ========== DOCUMENTATION ==========
print(f"{Colors.BLUE}DOCUMENTATION DISPONIBLE:{Colors.ENDC}")
print("- README_EMAIL_SYSTEM.md      → Guide de navigation")
print("- SYSTEME_EMAIL_GUIDE.md      → Guide technique détaillé")
print("- SETUP_ETAPES.md              → Étapes d'installation")
print(f"\n{Colors.BOLD}{Colors.BLUE}Pour plus d'infos: Voir README_EMAIL_SYSTEM.md{Colors.ENDC}\n")

sys.exit(0 if percentage == 100 else 1)
