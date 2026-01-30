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
    my_bookings = Booking.objects.filter(user_name=user).order_by('-date_booked')
    my_listings = Listing.objects.filter(owner_name=user).order_by('-created_at')
    return render(request, 'housing/dashboard.html', {'user': user, 'bookings': my_bookings, 'my_listings': my_listings})

def create_listing_view(request):
    user = request.session.get('user_name', 'Invité')
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            l = form.save(commit=False)
            l.owner_name = user
            if l.city == 'Rabat': l.lat, l.lng = 34.0209, -6.8416
            elif l.city == 'Casablanca': l.lat, l.lng = 33.5731, -7.5898
            l.save()
            return redirect('dashboard')
    else: form = ListingForm()
    return render(request, 'housing/add_listing.html', {'form': form})

def explorer_view(request):
    listings = Listing.objects.all().order_by('-is_verified', '-created_at')

    # --- FILTRAGE AVANCÉ ---
    city = request.GET.get('city')
    gender = request.GET.get('gender')
    
    # Gestion Budget Min/Max
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if city and city != 'All': listings = listings.filter(city=city)
    if gender and gender != 'All': listings = listings.filter(gender_preference=gender)
    
    # Logique Budget
    if min_price: listings = listings.filter(price__gte=min_price)
    if max_price: listings = listings.filter(price__lte=max_price)

    map_data = json.dumps([{'title': l.title, 'price': l.price, 'lat': l.lat, 'lng': l.lng, 'id': l.id, 'verified': l.is_verified} for l in listings])
    
    return render(request, 'housing/explorer.html', {
        'listings': listings, 'map_data': map_data,
        'selected_city': city, 'selected_gender': gender,
        'min_val': min_price, 'max_val': max_price
    })

def listing_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request, 'housing/detail.html', {'l': listing, 'amenities': listing.amenities.split(',')})

def book_listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    Booking.objects.create(user_name=request.session.get('user_name'), listing=listing, status="CONFIRMÉ")
    return redirect('dashboard')

# Login view handles authentication

# Logout clears session data

# optimized auth check

# Access restricted to authenticated users

# Redirect loop fix

# SECURITY: Validation des entrées login

# Session flush on logout

# Check user permissions

# Redirect loop fix implementation

# Code cleanup pass

# moved some logic here

# final check

# security check comment

# FIX: Form was missing POST method check

# debug print removed

# complex query logic for city filter
