from django.contrib import admin
from .models import City, StudentHouse, Room, BookingRequest

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ("name",)

@admin.register(StudentHouse)
class StudentHouseAdmin(admin.ModelAdmin):
    list_display = ("name", "city")
    list_filter = ("city",)
    search_fields = ("name", "address")

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("number", "house", "floor", "room_type", "capacity", "occupied_places", "monthly_price")
    list_filter = ("house__city", "room_type", "floor")
    search_fields = ("number", "house__name")

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ("student", "room", "check_in", "status", "created_at")
    list_filter = ("status", "room__house__city")
    search_fields = ("student__username", "room__number", "room__house__name")
