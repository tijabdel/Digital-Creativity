from django.db import models
from django.conf import settings


class City(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class StudentHouse(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="houses")
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.name} - {self.city.name}"


class Room(models.Model):
    ROOM_TYPE = [
        ("studio", "Studio individuel"),
        ("double", "Chambre double"),
    ]

    house = models.ForeignKey(StudentHouse, on_delete=models.CASCADE, related_name="rooms")
    number = models.CharField(max_length=20)
    floor = models.PositiveIntegerField()
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE)
    capacity = models.PositiveIntegerField(default=1)
    occupied_places = models.PositiveIntegerField(default=0)
    monthly_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.house.name} - Room {self.number} (Floor {self.floor})"

    @property
    def is_available(self):
        return self.occupied_places < self.capacity
    
    def available_places(self):
        return self.capacity - self.occupied_places

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["house", "number"],
                name="unique_room_number_per_house"
            ),
        ]

class BookingRequest(models.Model):
    STATUS = [
        ("pending", "En attente"),
        ("accepted", "Acceptée"),
        ("rejected", "Refusée"),
    ]

    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="requests")
    check_in = models.DateField()  # ✅ only check-in date
    status = models.CharField(max_length=10, choices=STATUS, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} -> {self.room} ({self.status})"
