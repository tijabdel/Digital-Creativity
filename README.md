# 🏠 StudentHouse (Projet Académique)

**Module : Digital Creativity**

Bonjour ! Voici le guide complet pour installer et tester **StudentHouse**, notre solution interactive pour le logement étudiant au Maroc.

---

## 👥 L'Équipe Projet (Groupe 4)

Nous sommes quatre étudiants de l'**ENSA** ayant collaboré sur ce projet :

* **Assia Belaissia**
* **Salami Saad**
* **Tijani Abdelbarie**
* **Fatima Ezzahra Arfaoui**

---

## 💡 Concept

Trouver un logement au Maroc est un défi. **StudentHouse** centralise les offres de manière fiable :
* **Réalisme** : Intégration de résidences réelles (*Bayt Al Maârifa*, *Ziraoui*...).
* **Respect culturel** : Filtrage par genre (**Filles / Garçons**).
* **Interaction** : Mise en relation simplifiée via **WhatsApp**.

---

## 🛠️ Guide d'Installation (Étape par Étape)

Ouvrez votre terminal (PowerShell ou Bash) et suivez ces étapes dans l'ordre :

### 1. Récupérer le projet
Clonez le dépôt GitHub sur votre machine :
\\\ash
git clone https://github.com/tijabdel/Digital-Creativity.git
cd Digital-Creativity
\\\

### 2. Configurer l'environnement
Créez et activez un environnement virtuel, puis installez les bibliothèques :
\\\ash
# Création de l'environnement
python -m venv venv

# Activation (Windows)
.\venv\Scripts\activate

# Installation des dépendances
pip install -r requirements.txt
\\\

### 3. Initialiser la Base de Données
Cette étape crée les tables et injecte les annonces réelles pour la démonstration :
\\\ash
python manage.py makemigrations housing
python manage.py migrate
python seed.py
\\\

### 4. Lancer l'application
\\\ash
python manage.py runserver
\\\
👉 Accès local : **http://127.0.0.1:8000/**

---

## 🎨 Choix du Design
Le projet utilise un **Light Mode** minimaliste (inspiré d'Airbnb) pour garantir une lisibilité optimale. La carte interactive utilise *Leaflet.js* avec un rendu clair pour une navigation fluide entre les quartiers étudiants.

---
*Projet réalisé avec passion par notre équipe à l'ENSA Tanger.*




