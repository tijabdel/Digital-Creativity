from django.contrib import admin
from .models import Listing, Profile, Booking

admin.site.site_header = 'StudentHouse Administration'
admin.site.site_title = 'StudentHouse Admin'
admin.site.index_title = 'Gestion du site'

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'price', 'type', 'is_verified')
    list_filter = ('city', 'type', 'is_verified')
    search_fields = ('title', 'description')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'is_student')
    search_fields = ('user__username', 'phone')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'listing', 'created_at')
