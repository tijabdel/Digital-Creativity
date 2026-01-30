from django.db import models
from django.utils import timezone

class Listing(models.Model):
    CITY_CHOICES = [
        ('Rabat', 'Rabat'), ('Casablanca', 'Casablanca'), ('Marrakech', 'Marrakech'),
        ('Tanger', 'Tanger'), ('Agadir', 'Agadir'), ('Ifrane', 'Ifrane'),
        ('Fes', 'Fès'), ('Meknes', 'Meknès'), ('Kenitra', 'Kénitra')
    ]
    
    TYPE_CHOICES = [
        ('STUDIO', 'Studio Individuel'),
        ('COLOC', 'Colocation (Chambre)'),
        ('RESIDENCE', 'Résidence Étudiante (Privée/Publique)')
    ]

    GENDER_CHOICES = [
        ('Filles', 'Réservé aux Étudiantes (Filles)'), 
        ('Garçons', 'Réservé aux Étudiants (Garçons)')
    ]
    
    # Info de base
    title = models.CharField(max_length=200, verbose_name="Titre de l'annonce")
    city = models.CharField(max_length=50, choices=CITY_CHOICES, verbose_name="Ville")
    university_nearby = models.CharField(max_length=100, default="Université", verbose_name="Proche de")
    price = models.IntegerField(verbose_name="Prix (DH/mois)")
    is_bills_included = models.BooleanField(default=False, verbose_name="Charges comprises")
    
    # Critères
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='STUDIO')
    gender_preference = models.CharField(max_length=20, choices=GENDER_CHOICES, default="Garçons", verbose_name="Genre")
    
    # Détails
    description = models.TextField(default="Description du logement...")
    amenities = models.CharField(max_length=300, default="Wifi,Sécurité", verbose_name="Équipements")
    
    # Contact & Media
    whatsapp_number = models.CharField(max_length=20, default="212600000000", help_text="Format: 2126XXXXXXXX")
    image_url = models.URLField(default="https://images.unsplash.com/photo-1555854877-bab0e564b8d5?w=800")
    
    # Technique
    lat = models.FloatField(default=33.5731)
    lng = models.FloatField(default=-7.5898)
    created_at = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False) # True = Admin/Residence officielle, False = Étudiant
    owner_name = models.CharField(max_length=100, default="Anonyme")

    def __str__(self): return self.title

class Booking(models.Model):
    user_name = models.CharField(max_length=100)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="EN ATTENTE")

# User data protection

# Models ordered by dependency

# added ordering

    class Meta: ordering = ['-created_at']

# verbose name fix

# verified by tijani
