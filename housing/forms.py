from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'city', 'university_nearby', 'price', 'type', 'gender_preference', 'whatsapp_number', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Cherche colocataire Maarif'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'university_nearby': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Près de ENCG'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'gender_preference': forms.Select(attrs={'class': 'form-control'}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2126...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# label tweaks

# price validation
