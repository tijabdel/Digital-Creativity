from django.shortcuts import render

# --- MOCK DATA FOR DESIGNER ---
# Use this data to style your cards. No database required.
mock_listings = [
    {
        'id': 1,
        'title': 'Résidence Al Amana',
        'city': 'Rabat',
        'price': 2200,
        'type': 'STUDIO',
        'gender': 'Filles',
        'image': 'https://images.unsplash.com/photo-1555854877-bab0e564b8d5?w=600',
        'uni': 'UM5 Agdal',
        'tags': ['Sécurisé', 'Wifi']
    },
    {
        'id': 2,
        'title': 'Dar Talib Maarif',
        'city': 'Casablanca',
        'price': 1600,
        'type': 'COLOC',
        'gender': 'Garçons',
        'image': 'https://images.unsplash.com/photo-1522771753035-4a50c9a21c00?w=600',
        'uni': 'Fac Médecine',
        'tags': ['Mosquée Proche', 'Économique']
    },
    {
        'id': 3,
        'title': 'Studio Premium Ifrane',
        'city': 'Ifrane',
        'price': 3000,
        'type': 'STUDIO',
        'gender': 'Filles',
        'image': 'https://images.unsplash.com/photo-1596204099684-2661c9255a6d?w=600',
        'uni': 'AUI',
        'tags': ['Chauffage', 'Neuf']
    }
]

def login_view(request):
    return render(request, 'login.html')

def explorer_view(request):
    # We pass the mock data to your HTML here
    return render(request, 'explorer.html', {'listings': mock_listings})

def detail_view(request, id):
    # Find the listing by ID (Mock logic)
    listing = next((item for item in mock_listings if item['id'] == id), mock_listings[0])
    return render(request, 'detail.html', {'l': listing})
