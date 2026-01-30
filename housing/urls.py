from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('explorer/', views.explorer, name='explorer'),
    path('listing/<int:pk>/', views.detail, name='detail'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('create/', views.create_listing, name='create_listing'),
]
