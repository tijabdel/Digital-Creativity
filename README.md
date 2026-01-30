# 🏠 StudentHouse (Projet Académique)

**Module : Digital Creativity**

Bonjour ! Voici le rendu final de notre projet **StudentHouse**, une solution interactive pour le logement étudiant au Maroc.

---

## 👥 L'Équipe Projet (Groupe 4)

Nous sommes quatre étudiants de l'**ENSA** ayant collaboré sur ce projet :

* **Assia Belaissia** (Frontend & Design Lead)
* **Salami Saad**
* **Tijani Abdelbarie**
* **Fatima Ezzahra Arfaoui**

---

## 💡 Concept & Vision

Trouver un logement au Maroc (Rabat, Casablanca, Tanger...) est un défi majeur pour tout étudiant. Notre application, **StudentHouse**, a pour but de centraliser les offres de manière fiable et interactive.

### Nos points forts :
1.  **Réalisme des données** : Intégration des résidences réelles (*Bayt Al Maârifa*, *Ziraoui*, *Campus Universiapolis*...).
2.  **Transparence** : Distinction claire entre les résidences officielles (Vérifiées) et les annonces de particuliers (Colocations).
3.  **Respect culturel** : Filtrage strict par genre (**Filles / Garçons**), essentiel dans le contexte marocain.
4.  **Interaction directe** : Mise en relation simplifiée via l'**API WhatsApp** avec les propriétaires.

---

## 🛠️ Guide d'Installation Rapide

### 1. Préparer l'environnement
\\\ash
# Activer l'environnement virtuel
.\venv\Scripts\activate

# Installer les outils nécessaires
pip install -r requirements.txt
\\\

### 2. Initialiser la Base de Données
Nous avons inclus un script de "Seeding" pour charger des exemples concrets dès le premier lancement.
\\\ash
python manage.py makemigrations housing
python manage.py migrate
python seed.py
\\\

### 3. Lancer l'application
\\\ash
python manage.py runserver
\\\
Accès local : **http://127.0.0.1:8000/**

---

## 🎨 Choix du Design

Nous avons opté pour un **Light Mode** minimaliste, inspiré des standards actuels (Airbnb, Apple). Ce choix permet une meilleure lisibilité des informations et met en valeur les photos des logements ainsi que la carte interactive (Leaflet.js).

---
*Projet réalisé avec passion par notre équipe à l'ENSA Tanger.*
