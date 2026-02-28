#!/usr/bin/env python
"""
Script pour corriger les titres et mettre à jour les vidéos existantes
"""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
sys.path.insert(0, '/home/star/Desktop/projet_production/API/backend')
django.setup()

from produition.models import Video

print("=" * 60)
print("🎬 MISE À JOUR DES VIDÉOS")
print("=" * 60)

videos = Video.objects.all()

for i, video in enumerate(videos, 1):
    filename = str(video.video_file.name).split('/')[-1]
    
    # Déterminer automatiquement le titre basé sur le nom du fichier
    if 'HYUNDAI' in filename.upper():
        new_title = 'HYUNDAI - Campagne Commerciale'
        category = 'hero'
    elif 'DADJU' in filename.upper():
        new_title = f'DADJU - Reine (Vidéo clip)'
        category = 'portfolio'
    else:
        new_title = filename.replace('.mp4', '').replace('_', ' ')
        category = 'other'
    
    # Mettre à jour la vidéo
    video.title = new_title
    if video.category == 'other':
        video.category = category
    
    video.save()
    
    print(f"\n✅ Vidéo {i} mise à jour:")
    print(f"    Titre: {video.title}")
    print(f"    Catégorie: {video.get_category_display()}")
    print(f"    Statut: {video.get_status_display()}")
    print(f"    Featured: {'✅ OUI' if video.is_featured else '❌ NON'}")
    print(f"    Fichier: {video.video_file.name}")

print("\n" + "=" * 60)
print("✅ Mise à jour terminée!")
print("=" * 60)

# Vérifier les vidéos finales
print("\n🎯 VÉRIFICATION FINALE:")
print("-" * 60)

hero_videos = Video.objects.filter(
    status='published',
    is_featured=True
).order_by('-order')[:1]

if hero_videos:
    video = hero_videos[0]
    print(f"✅ Vidéo héro trouvée: {video.title}")
    print(f"    URL du fichier: {video.video_file.url}")
    print(f"\n    Utilisez cette vidéo dans base.html avec:")
    print(f"    {{% if videos %}}")
    print(f"    <video autoplay muted loop playsinline>")
    print(f'        <source src="{{{{ videos.0.video_file.url }}}}" type="video/mp4">')
    print(f"    </video>")
    print(f"    {{% endif %}}")
else:
    print("❌ Aucune vidéo héro trouvée!")
