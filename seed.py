import os, django
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from housing.models import Listing

Listing.objects.all().delete()
print('🧹 Base de données nettoyée.')

# --- DONNÉES RÉELLES MAROC ---

# 1. RABAT (Madinat Al Irfane / Agdal)
Listing.objects.create(
    title="Bayt Al Maârifa - Studio Individuel",
    city="Rabat",
    university_nearby="UM5 / Madinat Al Irfane",
    price=1900,
    type="RESIDENCE",
    gender_preference="Filles",
    is_bills_included=True,
    is_verified=True,
    lat=33.9716, lng=-6.8656,
    description="Studio tout équipé dans la résidence officielle Bayt Al Maârifa. Sécurité 24/7, accès wifi, proche station tramway.",
    image_url="https://images.unsplash.com/photo-1555854877-bab0e564b8d5?w=800"
)
Listing.objects.create(
    title="Colocation Agdal Proche Tram",
    city="Rabat",
    university_nearby="Faculté des Sciences",
    price=1500,
    type="COLOC",
    gender_preference="Garçons",
    is_bills_included=False,
    is_verified=False, # Annonce particulier
    lat=34.0044, lng=-6.8488,
    description="Cherche colocataire sérieux. Appartement 3 chambres, salon, cuisine équipée. Quartier calme.",
    owner_name="Karim"
)

# 2. CASABLANCA (Maarif / Route El Jadida)
Listing.objects.create(
    title="Résidence Universitaire Ziraoui",
    city="Casablanca",
    university_nearby="Lycée Lyautey / Médecine",
    price=1700,
    type="RESIDENCE",
    gender_preference="Garçons",
    is_bills_included=True,
    is_verified=True,
    lat=33.5936, lng=-7.6322,
    description="Chambre individuelle dans résidence Ziraoui. Cadre studieux, bibliothèque et réfectoire sur place.",
    image_url="https://images.unsplash.com/photo-1596204099684-2661c9255a6d?w=800"
)
Listing.objects.create(
    title="Studio Haut Standing Anfa City",
    city="Casablanca",
    university_nearby="Université Mundiapolis",
    price=3500,
    type="STUDIO",
    gender_preference="Filles",
    is_bills_included=True,
    is_verified=True,
    lat=33.5595, lng=-7.6681,
    description="Studio neuf à Anfa City. Proche CFC. Meublé moderne, climatisation et fibre optique.",
    image_url="https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800"
)

# 3. TANGER (ENCG / Malabata)
Listing.objects.create(
    title="The Student House Tanger",
    city="Tanger",
    university_nearby="ENCG Tanger",
    price=2200,
    type="RESIDENCE",
    gender_preference="Garçons",
    is_bills_included=True,
    is_verified=True,
    lat=35.7663, lng=-5.8335,
    description="Résidence privée première cité à Tanger. Navette gratuite vers ENCG. Salle de sport incluse.",
)

# 4. AGADIR (Universiapolis)
Listing.objects.create(
    title="Campus Universiapolis",
    city="Agadir",
    university_nearby="Universiapolis",
    price=1800,
    type="RESIDENCE",
    gender_preference="Filles",
    is_bills_included=True,
    is_verified=True,
    lat=30.4061, lng=-9.5539,
    description="Logement au cœur du campus. Accès direct aux salles de cours et restaurants universitaires.",
)

# 5. IFRANE (AUI)
Listing.objects.create(
    title="Chambre Centre Ville Ifrane",
    city="Ifrane",
    university_nearby="Al Akhawayn (AUI)",
    price=2500,
    type="COLOC",
    gender_preference="Filles",
    is_bills_included=True,
    is_verified=False,
    lat=33.5366, lng=-5.1066,
    description="Chambre chaleureuse avec chauffage central (très important ici !). À 5min de la navette AUI.",
    owner_name="Salma"
)

print('✅ 7 Annonces Réalistes Importées (Rabat, Casa, Tanger, Agadir, Ifrane).')

# Added Residence Ziraoui (Casablanca) - Real Data

# Added Studios in Agdal (Rabat)
