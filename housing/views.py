from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Listing, Booking
from .forms import ListingForm

# --- ACCUEIL ---
def index(request):
    listings = Listing.objects.filter(is_verified=True).order_by('-created_at')[:3]
    return render(request, 'housing/index.html', {'listings': listings})

# --- EXPLORER ---
def explorer(request):
    listings = Listing.objects.all().order_by('-created_at')
    city_query = request.GET.get('city', '')
    type_query = request.GET.get('type', '')
    max_price = request.GET.get('max_price', '')

    if city_query:
        listings = listings.filter(city__icontains=city_query)
    if type_query and type_query != '':
        listings = listings.filter(type=type_query)
    if max_price:
        listings = listings.filter(price__lte=max_price)
        
    context = {
        'listings': listings,
        'current_city': city_query,
        'current_type': type_query,
        'current_max': max_price
    }
    return render(request, 'housing/explorer.html', context)

# --- DÉTAIL ---
def detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(f'/login/?next=/listing/{pk}/')
        Booking.objects.create(user=request.user, listing=listing, message=request.POST.get('message', ''))
        messages.success(request, "Demande envoyée !")
        return redirect('dashboard')
    return render(request, 'housing/detail.html', {'listing': listing})

# --- PUBLISH ---
@login_required(login_url='login')
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner_name = request.user.username
            listing.save()
            messages.success(request, "Annonce publiée !")
            return redirect('dashboard')
    else:
        form = ListingForm()
    return render(request, 'housing/create_listing.html', {'form': form})

# --- DASHBOARD ---
@login_required(login_url='login')
def dashboard_view(request):
    my_bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    my_listings = Listing.objects.filter(owner_name=request.user.username).order_by('-created_at')
    return render(request, 'housing/dashboard.html', {'bookings': my_bookings, 'listings': my_listings})

# --- AUTHENTIFICATION (FIXÉ) ---
def signup_view(request):
    # Correction ici : request.user au lieu de request.request.user
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Bienvenue sur StudentHouse !")
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    # Correction ici aussi
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.GET:
                return redirect(request.GET.get('next'))
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')
