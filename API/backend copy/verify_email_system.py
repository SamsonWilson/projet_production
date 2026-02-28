#!/usr/bin/env python
"""
SCRIPT DE VÉRIFICATION - SYSTÈME D'EMAIL KINÉRA
Vérifie que tous les composants sont correctement configurés.
"""

import os
import sys
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
sys.path.insert(0, str(Path(__file__).parent))

django.setup()

from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.management import call_command
import logging

# Configuration des couleurs pour la console
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def check(condition, message):
    """Affiche le résultat d'une vérification."""
    if condition:
        print(f"{Colors.GREEN}✓{Colors.ENDC} {message}")
        return True
    else:
        print(f"{Colors.RED}✗{Colors.ENDC} {message}")
        return False

def info(message):
    """Affiche une information."""
    print(f"{Colors.BLUE}ℹ{Colors.ENDC} {message}")

def header(title):
    """Affiche un titre de section."""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{title.center(60)}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.ENDC}\n")

def section(title):
    """Affiche un sous-titre."""
    print(f"\n{Colors.BOLD}{Colors.YELLOW}→ {title}{Colors.ENDC}")

# ============================================================================
# VÉRIFICATIONS
# ============================================================================

print(f"\n{Colors.BOLD}{Colors.CYAN}")
print("╔════════════════════════════════════════════════════════════╗")
print("║  VÉRIFICATION DU SYSTÈME D'EMAIL - KINÉRA FILM FIXERS      ║")
print("╚════════════════════════════════════════════════════════════╝")
print(f"{Colors.ENDC}")

results = {
    'configuration': [],
    'modeles': [],
    'fichiers': [],
    'database': [],
    'email': []
}

# ============================================================================
header("1. VÉRIFICATION DE LA CONFIGURATION DJANGO")
# ============================================================================

section("Base de données")
try:
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
    check(True, "Connexion à la base de données ✓")
    results['configuration'].append(True)
except Exception as e:
    check(False, f"Connexion à la base de données: {e}")
    results['configuration'].append(False)

section("Applications installées")
required_apps = ['django.contrib.contenttypes', 'django.contrib.auth', 'produition']
for app in required_apps:
    is_installed = app in settings.INSTALLED_APPS
    check(is_installed, f"Application '{app}' installée")
    results['configuration'].append(is_installed)

section("Configuration email")
check(hasattr(settings, 'EMAIL_BACKEND'), "EMAIL_BACKEND configuré")
check(hasattr(settings, 'DEFAULT_FROM_EMAIL'), "DEFAULT_FROM_EMAIL configuré")
check(hasattr(settings, 'ADMIN_EMAIL'), "ADMIN_EMAIL configuré")
results['configuration'].append(hasattr(settings, 'EMAIL_BACKEND'))
results['configuration'].append(hasattr(settings, 'DEFAULT_FROM_EMAIL'))
results['configuration'].append(hasattr(settings, 'ADMIN_EMAIL'))

# Afficher la config email actuelle
print(f"{Colors.BLUE}ℹ{Colors.ENDC} Backend email: {settings.EMAIL_BACKEND}")
print(f"{Colors.BLUE}ℹ{Colors.ENDC} Email de départ: {settings.DEFAULT_FROM_EMAIL}")
print(f"{Colors.BLUE}ℹ{Colors.ENDC} Email admin: {getattr(settings, 'ADMIN_EMAIL', 'Non défini')}")

# Déterminer le mode
if 'console' in settings.EMAIL_BACKEND:
    print(f"{Colors.YELLOW}⚠{Colors.ENDC} Mode DÉVELOPPEMENT: Emails peuvent s'afficher en console")
elif 'smtp' in settings.EMAIL_BACKEND:
    print(f"{Colors.GREEN}✓{Colors.ENDC} Mode PRODUCTION: Emails seront envoyés via SMTP")

# ============================================================================
header("2. VÉRIFICATION DES MODÈLES")
# ============================================================================

section("Modèle Message")
try:
    from produition.models import Message
    check(True, "Modèle Message importé avec succès")
    results['modeles'].append(True)
    
    # Vérifier les champs
    fields = [f.name for f in Message._meta.get_fields()]
    required_fields = ['sender_name', 'sender_email', 'subject', 'message', 
                     'category', 'status', 'email_sent', 'email_sent_at']
    
    for field in required_fields:
        field_exists = field in fields
        check(field_exists, f"Champ '{field}' existe")
        results['modeles'].append(field_exists)
        
except Exception as e:
    check(False, f"Erreur lors du chargement du modèle: {e}")
    results['modeles'].append(False)

# ============================================================================
header("3. VÉRIFICATION DES FICHIERS")
# ============================================================================

section("Fichiers Python")
files_to_check = [
    ('produition/models.py', 'Modèle Message'),
    ('produition/Forms/formsContact.py', 'Formulaire Contact'),
    ('produition/views/views_contact.py', 'Vues Contact'),
    ('produition/admin.py', 'Admin configuration'),
    ('produition/urls.py', 'URLs'),
]

for filepath, description in files_to_check:
    full_path = Path(__file__).parent / filepath
    file_exists = full_path.exists()
    check(file_exists, f"{description} ({filepath})")
    results['fichiers'].append(file_exists)

section("Fichiers templates email")
templates = [
    'emails/message_confirmation.html',
    'emails/message_admin_notification.html',
]

for template in templates:
    full_path = Path(__file__).parent / 'templates' / template
    file_exists = full_path.exists()
    check(file_exists, f"Template {template}")
    results['fichiers'].append(file_exists)

# ============================================================================
header("4. VÉRIFICATION DE LA BASE DE DONNÉES")
# ============================================================================

section("Table Message")
try:
    from django.db import connection
    from django.db.utils import OperationalError, ProgrammingError
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM produition_message;")
            count = cursor.fetchone()[0]
        check(True, f"Table 'produition_message' existe ({count} messages)")
        results['database'].append(True)
        info(f"Nombre de messages en base: {count}")
    except (OperationalError, ProgrammingError):
        check(False, "Table 'produition_message' n'existe pas - Exécutez: python manage.py migrate")
        results['database'].append(False)
except Exception as e:
    check(False, f"Erreur lors de la vérification de la table: {e}")
    results['database'].append(False)

# ============================================================================
header("5. VÉRIFICATION DE L'EMAIL")
# ============================================================================

section("Importation des modules")
try:
    from produition.Forms.formsContact import MessageForm
    check(True, "MessageForm importée")
    results['email'].append(True)
except Exception as e:
    check(False, f"Erreur lors de l'import de MessageForm: {e}")
    results['email'].append(False)

try:
    from produition.views.views_contact import send_email_to_sender, send_email_to_admin, ContactFormView
    check(True, "Fonctions d'email importées")
    results['email'].append(True)
except Exception as e:
    check(False, f"Erreur lors de l'import des fonctions email: {e}")
    results['email'].append(False)

section("Validation de la configuration email")
if 'console' in settings.EMAIL_BACKEND:
    check(True, "Backend console configuré pour développement")
    results['email'].append(True)
else:
    has_host = hasattr(settings, 'EMAIL_HOST') and settings.EMAIL_HOST
    has_port = hasattr(settings, 'EMAIL_PORT') and settings.EMAIL_PORT
    has_user = hasattr(settings, 'EMAIL_HOST_USER') and settings.EMAIL_HOST_USER
    
    check(has_host, "EMAIL_HOST configuré")
    check(has_port, "EMAIL_PORT configuré")
    check(has_user, "EMAIL_HOST_USER configuré")
    
    results['email'].append(has_host)
    results['email'].append(has_port)
    results['email'].append(has_user)

section("Structure du dossier logs")
logs_dir = Path(__file__).parent / 'logs'
logs_dir_exists = logs_dir.exists()
check(logs_dir_exists, f"Dossier /logs existe")
results['email'].append(logs_dir_exists)

if not logs_dir_exists:
    try:
        logs_dir.mkdir(parents=True, exist_ok=True)
        print(f"{Colors.GREEN}✓{Colors.ENDC} Dossier /logs créé")
    except Exception as e:
        print(f"{Colors.RED}✗{Colors.ENDC} Impossible de créer /logs: {e}")

# ============================================================================
header("6. TEST DE VALIDATION DE FORMULAIRE")
# ============================================================================

section("Test du formulaire")
try:
    from produition.Forms.formsContact import MessageForm
    
    # Test avec données valides
    form_data = {
        'sender_name': 'Jean Dupont',
        'sender_email': 'jean@example.com',
        'sender_phone': '+33612345678',
        'subject': 'Demande de devis',
        'message': 'Ceci est un message de test pour vérifier le système.',
        'category': 'devis'
    }
    
    form = MessageForm(data=form_data)
    form_valid = form.is_valid()
    check(form_valid, "Formulaire test valide")
    results['email'].append(form_valid)
    
    if not form_valid:
        print(f"{Colors.RED}✗{Colors.ENDC} Erreurs du formulaire:")
        for field, errors in form.errors.items():
            print(f"  - {field}: {errors}")
        
except Exception as e:
    check(False, f"Erreur lors du test du formulaire: {e}")
    results['email'].append(False)

# Test avec données invalides
try:
    invalid_data = {
        'sender_name': 'A',  # Trop court
        'sender_email': 'invalid-email',  # Email invalide
        'subject': 'Hi',  # Trop court
        'message': 'Court',  # Trop court
    }
    
    form = MessageForm(data=invalid_data)
    should_be_invalid = not form.is_valid()
    check(should_be_invalid, "Validation rejette les données invalides")
    results['email'].append(should_be_invalid)
    
except Exception as e:
    check(False, f"Erreur lors du test d'invalidation: {e}")
    results['email'].append(False)

# ============================================================================
header("7. RÉSUMÉ")
# ============================================================================

# Calculer les statistiques
total_checks = sum(len(v) for v in results.values())
total_passed = sum(sum(v) for v in results.values())

for category, checks in results.items():
    if checks:
        passed = sum(checks)
        total = len(checks)
        percentage = (passed / total * 100) if total > 0 else 0
        
        if percentage == 100:
            symbol = Colors.GREEN + "✓" + Colors.ENDC
        elif percentage >= 75:
            symbol = Colors.YELLOW + "⚠" + Colors.ENDC
        else:
            symbol = Colors.RED + "✗" + Colors.ENDC
            
        print(f"{symbol} {category.capitalize():20} {passed}/{total} ({percentage:.0f}%)")

print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.ENDC}")
percentage = (total_passed / total_checks * 100) if total_checks > 0 else 0

if percentage == 100:
    print(f"{Colors.GREEN}{Colors.BOLD}✓ TOUS LES TESTS SONT PASSÉS! {percentage:.0f}%{Colors.ENDC}")
    print(f"{Colors.GREEN}Votre système d'email est prêt à l'emploi!{Colors.ENDC}")
elif percentage >= 75:
    print(f"{Colors.YELLOW}{Colors.BOLD}⚠ PLUPART DES TESTS SONT PASSÉS {percentage:.0f}%{Colors.ENDC}")
    print(f"{Colors.YELLOW}Quelques petites corrections restent à faire.{Colors.ENDC}")
else:
    print(f"{Colors.RED}{Colors.BOLD}✗ CERTAINS TESTS ONT ÉCHOUÉ {percentage:.0f}%{Colors.ENDC}")
    print(f"{Colors.RED}Veuillez corriger les problèmes identifiés.{Colors.ENDC}")

print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.ENDC}\n")

# ============================================================================
header("PROCHAINES ÉTAPES")
# ============================================================================

if total_passed < total_checks:
    print(f"{Colors.RED}⚠ Problèmes détectés:{Colors.ENDC}\n")
    
    if not any(results['database']):
        print(f"{Colors.YELLOW}1. Exécutez:{Colors.ENDC}")
        print(f"   python manage.py makemigrations")
        print(f"   python manage.py migrate\n")
    
    if not all(results['fichiers']):
        print(f"{Colors.YELLOW}2. Vérifiez que tous les fichiers sont créés:{Colors.ENDC}")
        print(f"   - produition/models.py")
        print(f"   - produition/Forms/formsContact.py")
        print(f"   - produition/views/views_contact.py")
        print(f"   - templates/emails/message_confirmation.html")
        print(f"   - templates/emails/message_admin_notification.html\n")
else:
    print(f"{Colors.GREEN}✓ Système prêt! Prochaines étapes:{Colors.ENDC}\n")
    print(f"1. Exécuter: {Colors.BOLD}python manage.py runserver{Colors.ENDC}")
    print(f"2. Aller à: {Colors.BOLD}http://localhost:8000/admin/{Colors.ENDC}")
    print(f"3. Tester le formulaire contact")
    print(f"4. Vérifier les emails dans la console Django\n")

print(f"{Colors.BOLD}{Colors.CYAN}Pour plus d'infos, consulter: SYSTEME_EMAIL_GUIDE.md{Colors.ENDC}\n")

sys.exit(0 if percentage == 100 else 1)
