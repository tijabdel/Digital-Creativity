from django.core.management.base import BaseCommand
from housing.models import City, StudentHouse, Room


class Command(BaseCommand):
    help = "Seed realistic student housing data (Morocco)"

    def handle(self, *args, **options):

        
        # 1. Cities
        
        city_names = [
            "Tangier",
            "Rabat",
            "Casablanca",
            "Agadir",
            "Marrakech"
        ]

        cities = {}
        for name in city_names:
            city, _ = City.objects.get_or_create(name=name)
            cities[name] = city

        self.stdout.write(self.style.SUCCESS("Cities created"))

    
        # 2. Student Houses
        
        houses_data = [
            # Tangier
            ("Tangier University Student House", "Tangier", "Boukhalef Area"),
            ("Ibn Battuta Student Residence", "Tangier", "Malabata"),

            # Rabat
            ("Rabat Academic Student House", "Rabat", "Agdal District"),

            # Casablanca
            ("Casablanca Student Residence Center", "Casablanca", "Maarif"),
            ("Anfa Student Housing Complex", "Casablanca", "Anfa Place"),

            # Agadir
            ("Agadir University Student House", "Agadir", "Dakhla District"),

            # Marrakech
            ("Marrakech Student Campus Residence", "Marrakech", "Daoudiate"),
            ("Al Qadi Ayyad Student House", "Marrakech", "University Zone"),
        ]

        houses = []

        for name, city_name, address in houses_data:
            house, _ = StudentHouse.objects.get_or_create(
                name=name,
                city=cities[city_name],
                address=address
            )
            houses.append(house)

        self.stdout.write(self.style.SUCCESS("Student houses created"))

        
        # 3. Rooms
        
        for house in houses:
            for floor in range(1, 5):  # floors 1 → 4

                # Studios
                Room.objects.get_or_create(
                    house=house,
                    number=f"{floor}01",
                    floor=floor,
                    room_type="studio",
                    capacity=1,
                    monthly_price=2000,
                    occupied_places=0
                )

                Room.objects.get_or_create(
                    house=house,
                    number=f"{floor}02",
                    floor=floor,
                    room_type="studio",
                    capacity=1,
                    monthly_price=2000,
                    occupied_places=0
                )

                # Double rooms
                for i in range(3, 9):  # 6 rooms per floor
                    Room.objects.get_or_create(
                        house=house,
                        number=f"{floor}0{i}",
                        floor=floor,
                        room_type="double",
                        capacity=2,
                        monthly_price=1500,
                        occupied_places=0
                    )

        