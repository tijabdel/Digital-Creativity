from django.db import models

class Listing(models.Model):
    CITY_CHOICES = [
        ('Rabat', 'Rabat'), ('Casablanca', 'Casablanca'), ('Marrakech', 'Marrakech'),
        ('Tanger', 'Tanger'), ('Kenitra', 'Kenitra'), ('Agadir', 'Agadir'),
        ('Fes', 'Fès'), ('Meknes', 'Meknès'), ('Ifrane', 'Ifrane'), ('Oujda', 'Oujda')
    ]
    
    # STRICT GENDER CHOICES
    GENDER_CHOICES = [
        ('Filles', 'Réservé aux Étudiantes (Filles)'), 
        ('Garçons', 'Réservé aux Étudiants (Garçons)')
    ]
    
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    university_nearby = models.CharField(max_length=100, default="Université")
    price = models.IntegerField()
    is_bills_included = models.BooleanField(default=False)
    
    # Updated Logic
    gender_preference = models.CharField(max_length=20, choices=GENDER_CHOICES, default="Garçons")
    
    image_url = models.URLField()
    type = models.CharField(max_length=50) 
    tags = models.CharField(max_length=200) 
    lat = models.FloatField()
    lng = models.FloatField()
    description = models.TextField(default="Logement respectueux et calme.")
    amenities = models.CharField(max_length=300, default="Wifi,Sécurité")
    whatsapp_number = models.CharField(max_length=20, default="212600000000")

    def __str__(self): return self.title

class Booking(models.Model):
    user_name = models.CharField(max_length=100)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="EN ATTENTE")
