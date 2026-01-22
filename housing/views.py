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

def room_search(request):
    """
    Search available rooms with filters:
    city, house, room_type, floor, max_price
    """
    rooms = Room.objects.filter(occupied_places__lt=F("capacity")).select_related("house", "house__city")

    city_id = request.GET.get("city")
    house_id = request.GET.get("house")
    room_type = request.GET.get("type")
    floor = request.GET.get("floor")
    max_price = request.GET.get("max_price")

    if city_id:
        rooms = rooms.filter(house__city_id=city_id)
    if house_id:
        rooms = rooms.filter(house_id=house_id)
    if room_type in ["studio", "double"]:
        rooms = rooms.filter(room_type=room_type)
    if floor and floor.isdigit():
        rooms = rooms.filter(floor=int(floor))
    if max_price:
        try:
            rooms = rooms.filter(monthly_price__lte=float(max_price))
        except ValueError:
            pass

    cities = City.objects.all().order_by("name")
    houses = StudentHouse.objects.all().order_by("name")

    context = {
        "rooms": rooms.order_by("monthly_price", "house__name", "number"),
        "cities": cities,
        "houses": houses,
        "selected": {
            "city": city_id or "",
            "house": house_id or "",
            "type": room_type or "",
            "floor": floor or "",
            "max_price": max_price or "",
        }
    }
    return render(request, "housing/room_search.html", context)
    return render(request, "housing/book_result.html", {"msg": "Request sent ✅ (pending)"})
    return render(request, "housing/book_form.html", {"room": room})
