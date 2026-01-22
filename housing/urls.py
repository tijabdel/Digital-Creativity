from django.urls import path
from . import views

urlpatterns = [
    path("", views.city_list, name="city_list"),
    path("city/<int:city_id>/", views.house_list, name="house_list"),
    path("house/<int:house_id>/", views.available_rooms, name="available_rooms"),
    path("book/<int:room_id>/", views.book_room, name="book_room"),
    path("search/", views.room_search, name="room_search"),
]
