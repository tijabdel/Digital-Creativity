from django.contrib import admin
from django.urls import path, include
from housing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add/', views.create_listing_view, name='add_listing'), # Nouvelle route
    path('explorer/', views.explorer_view, name='explorer'),
    path('listing/<int:id>/', views.listing_detail, name='listing_detail'),
    path('book/<int:id>/', views.book_listing, name='book_listing'),
]

# STRUCTURE: Reorganized URL patterns for better scalability
