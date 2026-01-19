from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.contrib.auth.decorators import login_required

from .models import City, StudentHouse, Room, BookingRequest


def city_list(request):
    cities = City.objects.all().order_by("name")
    return render(request, "housing/city_list.html", {"cities": cities})


def house_list(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    houses = StudentHouse.objects.filter(city=city).order_by("name")
    return render(request, "housing/house_list.html", {"city": city, "houses": houses})


def available_rooms(request, house_id):
    house = get_object_or_404(StudentHouse, pk=house_id)
    rooms = (
        Room.objects.filter(house=house, occupied_places__lt=F("capacity"))
        .order_by("floor", "number")
    )
    return render(request, "housing/available_rooms.html", {"house": house, "rooms": rooms})


@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    if request.method == "POST":
        check_in = request.POST.get("check_in")

        BookingRequest.objects.create(
            student=request.user,
            room=room,
            check_in=check_in,
            status="pending",
        )

        return render(request, "housing/book_result.html", {"msg": "Request sent ✅ (pending)"})

    return render(request, "housing/book_form.html", {"room": room})
