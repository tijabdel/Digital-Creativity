from django.shortcuts import render, redirect, get_object_or_404
from .models import Listing, Booking
from .forms import ListingForm
import json

def login_view(request):
    if request.method == "POST":
        request.session['user_name'] = request.POST.get('username', 'Etudiant')
        return redirect('dashboard')
    return render(request, 'housing/login.html')

def dashboard_view(request):
    user = request.session.get('user_name', 'Invité')
    # Les réservations de l'utilisateur
    my_bookings = Booking.objects.filter(user_name=user).order_by('-date_booked')
    # Les annonces publiées par l'utilisateur
    my_listings = Listing.objects.filter(owner_name=user).order_by('-created_at')
    
    return render(request, 'housing/dashboard.html', {
        'user': user, 
        'bookings': my_bookings,
        'my_listings': my_listings
    })

def create_listing_view(request):
    user = request.session.get('user_name', 'Invité')
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner_name = user
            # On met des coordonnées par défaut selon la ville pour l'exemple
            if listing.city == 'Rabat':
                listing.lat, listing.lng = 34.0209, -6.8416
            elif listing.city == 'Casablanca':
                listing.lat, listing.lng = 33.5731, -7.5898
            # ... (autres villes)
            listing.save()
            return redirect('dashboard')
    else:
        form = ListingForm()
    return render(request, 'housing/add_listing.html', {'form': form})

def explorer_view(request):
    listings = Listing.objects.all().order_by('-is_verified', '-created_at')

    # Filtres
    city = request.GET.get('city')
    type_l = request.GET.get('type')
    gender = request.GET.get('gender')
    price = request.GET.get('price')

    if city and city != 'All': listings = listings.filter(city=city)
    if type_l and type_l != 'All': listings = listings.filter(type=type_l)
    if gender and gender != 'All': listings = listings.filter(gender_preference=gender)
    if price: listings = listings.filter(price__lte=price)

    map_data = json.dumps([
        {'title': l.title, 'price': l.price, 'lat': l.lat, 'lng': l.lng, 'id': l.id, 'city': l.city, 'verified': l.is_verified} 
        for l in listings
    ])
    
    return render(request, 'housing/explorer.html', {
        'listings': listings, 
        'map_data': map_data,
        'selected_city': city,
        'selected_type': type_l,
        'selected_gender': gender
    })

def listing_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    amenities = listing.amenities.split(',')
    return render(request, 'housing/detail.html', {'l': listing, 'amenities': amenities})

def book_listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    user = request.session.get('user_name', 'Etudiant')
    Booking.objects.create(user_name=user, listing=listing, status="CONFIRMÉ")
    return redirect('dashboard')
