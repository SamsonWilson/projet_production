#!/usr/bin/env python
"""
Script de diagnostic pour la vidéo héro dans base.html
Vérifie s'il y a des vidéos et en crée une de test si nécessaire
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
sys.path.insert(0, '/home/star/Desktop/projet_production/API/backend')
django.setup()

from produition.models import Video, CustomUser
from django.utils import timezone

print("=" * 60)
print("🔍 DIAGNOSTIC - Vidéo Héro dans base.html")
print("=" * 60)

# 1. Vérifier le nombre de vidéos en base
print("\n1️⃣ VÉRIFICATION DES VIDÉOS EN BASE DE DONNÉES")
print("-" * 60)

total_videos = Video.objects.count()
published_videos = Video.objects.filter(status='published').count()
featured_videos = Video.objects.filter(is_featured=True).count()
published_featured = Video.objects.filter(status='published', is_featured=True).count()

print(f"   Total de vidéos: {total_videos}")
print(f"   Vidéos publiées: {published_videos}")
print(f"   Vidéos en avant (featured): {featured_videos}")
print(f"   Vidéos publiées ET en avant: {published_featured} ⭐")

# 2. Lister les vidéos existantes
print("\n2️⃣ VIDÉOS EXISTANTES")
print("-" * 60)

videos = Video.objects.all()
if videos:
    for i, video in enumerate(videos, 1):
        print(f"\n   {i}. {video.title}")
        print(f"      Status: {video.get_status_display()}")
        print(f"      Featured: {'✅ OUI' if video.is_featured else '❌ NON'}")
        print(f"      Catégorie: {video.get_category_display()}")
        print(f"      Fichier: {video.video_file.name if video.video_file else 'Aucun'}")
else:
    print("   ❌ AUCUNE VIDÉO EN BASE DE DONNÉES!")

# 3. Vérifier les vidéos que le template cherche
print("\n3️⃣ VIDÉOS QUE LE TEMPLATE BASE.HTML VA AFFICHER")
print("-" * 60)

hero_videos = Video.objects.filter(
    status='published',
    is_featured=True
).order_by('-order')[:1]

if hero_videos:
    for video in hero_videos:
        print(f"   ✅ Vidéo trouvée: {video.title}")
        print(f"      Fichier: {video.video_file.url if video.video_file else 'Aucun'}")
else:
    print("   ❌ AUCUNE VIDÉO TROUVÉE!")
    print("      (Besoin: status='published' ET is_featured=True)")

# 4. Vérifier les utilisateurs
print("\n4️⃣ VÉRIFICATION DES UTILISATEURS")
print("-" * 60)

users = CustomUser.objects.filter(is_staff=True)
print(f"   Utilisateurs staff: {users.count()}")
if users:
    for user in users:
        print(f"   - {user.username} ({user.email})")
else:
    print("   ⚠️  Aucun utilisateur staff trouvé!")

# 5. Proposer une solution
print("\n5️⃣ 💡 SOLUTION")
print("-" * 60)

if not published_featured:
    print("   Le problème: Aucune vidéo avec:")
    print("   - status = 'published'")
    print("   - is_featured = True")
    print()
    print("   Solutions:")
    print("   a) Créer une vidéo via l'interface: /videos/ajouter/")
    print("   b) Créer une vidéo via l'admin: /admin/produition/video/")
    print("   c) Lancer le script create_test_video.py:")
    print("      /home/star/Desktop/projet_production/API/venv/bin/python create_test_video.py")
else:
    print("   ✅ Les vidéos sont correctement configurées!")
    print("   🔍 Vérifiez:")
    print("   1. Que le fichier vidéo existe")
    print("   2. Les permissions sur le dossier /media/")
    print("   3. La console du navigateur (F12) pour les erreurs")

print("\n" + "=" * 60)
print("✅ Diagnostic terminé")
print("=" * 60)
