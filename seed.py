import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from housing.models import Listing

Listing.objects.all().delete()

# Descriptions respectueuses
desc_filles = "Résidence exclusivement réservée aux étudiantes. Environnement calme, sécurisé 24/7 avec gardien. Interdiction formelle aux invités masculins."
desc_garcons = "Logement pour étudiants garçons. Proche des facultés et de la mosquée. Ambiance studieuse."

data = [
    {
        'title': 'Résidence Al Amana', 'city': 'Rabat', 'uni': 'UM5 Agdal', 'p': 2200, 
        'type': 'STUDIO', 'tags': 'Sécurisé Calme', 'bills': True, 'gen': 'Filles',
        'img': 'https://images.unsplash.com/photo-1555854877-bab0e564b8d5?w=600',
        'lat': 34.00, 'lng': -6.85, 'desc': desc_filles
    },
    {
        'title': 'Dar Talib Maarif', 'city': 'Casablanca', 'uni': 'Faculté Médecine', 'p': 1600, 
        'type': 'COLOC', 'tags': 'Mosquée Proche', 'bills': False, 'gen': 'Garçons',
        'img': 'https://images.unsplash.com/photo-1522771753035-4a50c9a21c00?w=600',
        'lat': 33.58, 'lng': -7.63, 'desc': desc_garcons
    },
    {
        'title': 'Studio Ensoleillé Ifrane', 'city': 'Ifrane', 'uni': 'AUI', 'p': 2800, 
        'type': 'STUDIO', 'tags': 'Chauffage', 'bills': True, 'gen': 'Filles',
        'img': 'https://images.unsplash.com/photo-1596204099684-2661c9255a6d?w=600',
        'lat': 33.53, 'lng': -5.11, 'desc': desc_filles
    },
    {
        'title': 'Appartement Ibn Batouta', 'city': 'Tanger', 'uni': 'ENCG Tanger', 'p': 2400, 
        'type': 'COLOC', 'tags': 'Wifi Fibre', 'bills': False, 'gen': 'Garçons',
        'img': 'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=600',
        'lat': 35.76, 'lng': -5.83, 'desc': desc_garcons
    }
]

for d in data:
    Listing.objects.create(
        title=d['title'], city=d['city'], university_nearby=d['uni'], price=d['p'],
        type=d['type'], tags=d['tags'], is_bills_included=d['bills'], gender_preference=d['gen'],
        image_url=d['img'], lat=d['lat'], lng=d['lng'], description=d['desc'],
        whatsapp_number="212600000000"
    )
print('✅ Listings Loaded (Strict Separation Applied)')
