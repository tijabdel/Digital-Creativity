from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('explorer/', views.explorer_view, name='explorer'),
    path('listing/<int:id>/', views.listing_detail, name='listing_detail'), # NEW
    path('book/<int:id>/', views.book_listing, name='book_listing'), # NEW
]

# Auth routes defined

# Route de déconnexion sécurisée

# cleaning urls

# fixed trailing slash
