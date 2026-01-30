from django.contrib import admin
from django.urls import path
from housing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('explorer/', views.explorer_view, name='explorer'),
    path('listing/<int:id>/', views.detail_view, name='detail'),
]
