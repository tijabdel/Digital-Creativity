import os
import django
import random

# 1. Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from housing.models import Listing

# 2. Nettoyage
print('🧹 Nettoyage de la base de données...')
Listing.objects.all().delete()

# 3. Les Données (Descriptions conservées, Images retirées)
listings_data = [
    # --- RABAT ---
    {
        'title': 'Chambre Solo - Madinat Al Irfane',
        'description': '🔥 LE SPOT ÉTUDIANT ! Chambre rénovée juste à côté de l\'ENSIAS et de la Fac de Médecine. Ambiance calme pour réviser, WiFi Fibre optique inclus. Douche commune mais propre. 5min à pied du Tram.',
        'price': 1600,
        'city': 'Rabat',
        'type': 'Chambre',
        'is_verified': True,
        'lat': 33.9785, 'lng': -6.8654,
        'owner': 'Mme Tazi (Super Hôte)'
    },
    {
        'title': 'Coloc Agdal (Filles) - Avenue de France',
        'description': 'Cherche 4ème colocataire (fille) pour grand appart à l\'Agdal. Juste au-dessus du McDo ! Salon géant avec Netflix, cuisine équipée. Loyer inclut syndic et eau. Ambiance chill mais sérieuse.',
        'price': 2200,
        'city': 'Rabat',
        'type': 'Appartement',
        'is_verified': False,
        'lat': 34.0045, 'lng': -6.8492,
        'owner': 'Sarah (Étudiante)'
    },
    {
        'title': 'Petit Studio Océan - Pas cher',
        'description': 'Petit studio indépendant quartier Océan. Idéal petit budget. Pas le grand luxe mais fonctionnel. Proche bus et taxis. Convient pour étudiant FST ou Fac des Lettres.',
        'price': 1800,
        'city': 'Rabat',
        'type': 'Studio',
        'is_verified': False,
        'lat': 34.0224, 'lng': -6.8351,
        'owner': 'Mr Benani'
    },

    # --- CASABLANCA ---
    {
        'title': 'Studio Maârif - "The Place to Be"',
        'description': 'Studio moderne à 2min du Twin Center. Pour étudiant(e) qui veut être au centre de tout. Concierge 24/7, ascenseur, cuisine américaine. Cher mais top qualité.',
        'price': 4500,
        'city': 'Casablanca',
        'type': 'Studio',
        'is_verified': False,
        'lat': 33.5855, 'lng': -7.6373,
        'owner': 'Agence Immo Casa'
    },
    {
        'title': 'Chambre chez l\'habitant - Oulfa',
        'description': 'Famille loue une chambre propre avec bureau pour étudiant sérieux. Quartier Oulfa (Hay Hassani), accès direct en bus à la Fac Route El Jadida et HEM. Repas possibles.',
        'price': 1200,
        'city': 'Casablanca',
        'type': 'Chambre',
        'is_verified': True,
        'lat': 33.5539, 'lng': -7.6622,
        'owner': 'Famille El Idrissi'
    },
    {
        'title': 'Coloc Garçons Sidi Maârouf - Nearshore',
        'description': 'Appart pour Geeks et Ingénieurs ! Proche Casanearshore. Fibre 100 Méga installée. On cherche un 3ème profil tech. Calme absolu pour coder la nuit.',
        'price': 1500,
        'city': 'Casablanca',
        'type': 'Appartement',
        'is_verified': False,
        'lat': 33.5356, 'lng': -7.6528,
        'owner': 'Simo (Dev)'
    },

    # --- TANGER ---
    {
        'title': 'Appart Boukhalef - Face à l\'ENSA',
        'description': 'Littéralement à 2 minutes de l\'ENSA et la FST en pyjama. Résidence Al Amana sécurisée. 2 chambres, salon marocain. Idéal pour groupe de 3 ou 4 étudiants.',
        'price': 2500,
        'city': 'Tanger',
        'type': 'Appartement',
        'is_verified': True,
        'lat': 35.7369, 'lng': -5.8941,
        'owner': 'Haj Boukhalef'
    },
    {
        'title': 'Coloc Vue Mer - Malabata',
        'description': 'Grand luxe à petit prix si on partage ! Appartement vue sur mer, proche Gare TGV et City Mall. Pour étudiantes ENCG Tanger. 3 Chambres dispos.',
        'price': 1600,
        'city': 'Tanger',
        'type': 'Appartement',
        'is_verified': False,
        'lat': 35.7765, 'lng': -5.7942,
        'owner': 'Mme Alaoui'
    },
    {
        'title': 'Studio Centre Ville - Iberia',
        'description': 'Studio cosy pour étudiant solitaire. Quartier Iberia, tout est à côté (cafés, snacks, taxis). Loyer un peu cher mais zéro transport à payer.',
        'price': 2800,
        'city': 'Tanger',
        'type': 'Studio',
        'is_verified': False,
        'lat': 35.7801, 'lng': -5.8123,
        'owner': 'Agence du Nord'
    },

    # --- IFRANE ---
    {
        'title': 'Chalet Bois - Près AUI (Al Akhawayn)',
        'description': 'Le rêve Ifranais. Chalet avec cheminée pour l\'hiver. À 10min à pied du campus AUI. Parfait pour colocation à 4. Chauffage central inclus (important !).',
        'price': 5000,
        'city': 'Ifrane',
        'type': 'Maison',
        'is_verified': True,
        'lat': 33.5366, 'lng': -5.1102,
        'owner': 'AUI Housing'
    }
]

# 4. Injection
print(f'🏗️ Création de {len(listings_data)} annonces (Mode Texte)...')

for data in listings_data:
    Listing.objects.create(
        title=data['title'],
        description=data['description'],
        price=data['price'],
        city=data['city'],
        type=data['type'],
        is_verified=data['is_verified'],
        lat=data['lat'],
        lng=data['lng'],
        owner_name=data['owner'],
        # image_url supprimé ou vide pour ne pas avoir de photo
        image_url='', 
        gender_preference=random.choice(['Mixte', 'Filles', 'Garçons'])
    )
    print(f"  ✅ Ajouté : {data['title']}")

print('\n✨ BASE DE DONNÉES MISE À JOUR (SANS PHOTOS) !')
