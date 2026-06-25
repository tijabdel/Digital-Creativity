from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
    else:
        if not hasattr(instance, 'profile'):
            Profile.objects.create(user=instance)
        instance.profile.save()

class Listing(models.Model):
    TYPE_CHOICES = [
        ('Colocation', 'Colocation'),
        ('Studio', 'Studio'),
        ('Appartement', 'Appartement'),
        ('Residence', 'Résidence Étudiante'),
        ('Chambre', 'Chambre chez l\'habitant'),
    ]

    GENDER_CHOICES = [
        ('Mixte', 'Mixte'),
        ('Filles', 'Filles'),
        ('Garçons', 'Garçons'),
    ]

    title = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Prix (DH)")
    city = models.CharField(max_length=100, verbose_name="Ville")
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Studio')

    university_nearby = models.CharField(max_length=200, blank=True, verbose_name="Université proche")
    whatsapp_number = models.CharField(max_length=20, default="+212600000000", verbose_name="WhatsApp")
    image_url = models.CharField(max_length=500, verbose_name="Lien Image (URL)", default="https://images.unsplash.com/photo-1522708323590-d24dbb6b0267")

    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    gender_preference = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='Mixte'
    )

    is_verified = models.BooleanField(default=False)
    owner_name = models.CharField(max_length=100, default="Anonyme")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"
