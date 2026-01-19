from django.contrib import admin
from .models import City, StudentHouse, Room, BookingRequest


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ("student", "room", "status", "check_in")
    list_filter = ("status",)

    def save_model(self, request, obj, form, change):
        if change:
            old = BookingRequest.objects.get(pk=obj.pk)

            # If admin ACCEPTS booking
            if old.status != "accepted" and obj.status == "accepted":
                room = obj.room
                room.occupied_places += 1
                room.save()

        super().save_model(request, obj, form, change)


admin.site.register(City)
admin.site.register(StudentHouse)
admin.site.register(Room)
