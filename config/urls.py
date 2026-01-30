from django.contrib import admin
from django.urls import path
from housing import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('explorer/', views.explorer, name='explorer'),
    
    # ON ACCEPTE LES DEUX NOMS POUR LA MÊME PAGE
    path('publish/', views.create_listing, name='create_listing'), # Nouveau nom
    path('create/', views.create_listing, name='create_listing_old'), # Ancien nom (celui que tu cherches)
    
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('listing/<int:pk>/', views.detail, name='detail'),
    
    # AUTH
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

# Gestion des images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
