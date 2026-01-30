# 🏠 StudentHouse (Projet 'Sakan')

Bonjour! Voici le code source de notre projet **StudentHouse**.
C'est une plateforme conçue pour aider les étudiants marocains (Rabat, Casa, Tanger...) à trouver des logements sécurisés et adaptés à leur budget.

Le design est inspiré d'une esthétique "Neon/Dark Mode" pour rendre l'expérience utilisateur moderne et agréable.

---

## 🛠️ Prérequis

Avant de lancer le projet, assurez-vous d'avoir **Python** installé sur votre machine.

## 🚀 Comment lancer l'application (Guide Rapide)

Suivez ces étapes simples pour tester le site sur votre ordinateur :

### 1. Activer l'environnement
Si vous êtes sur Windows (PowerShell), tapez :
\\\ash
.\venv\Scripts\activate
\\\

### 2. Installer les dépendances
Installez les bibliothèques nécessaires (Django, Leaflet...) :
\\\ash
pip install -r requirements.txt
\\\

### 3. Préparer la Base de Données
Si c'est la première fois que vous lancez le projet :
\\\ash
python manage.py migrate
python seed.py
\\\
*(Le script \seed.py\ va remplir le site avec de fausses annonces pour Rabat, Casa et Ifrane afin que vous ayez du contenu à visiter)*

### 4. Lancer le Serveur
\\\ash
python manage.py runserver
\\\

Ensuite, ouvrez votre navigateur et allez sur : **http://127.0.0.1:8000/**

---

## 🔐 Identifiants de Test

Pour accéder au tableau de bord "Quest Log", vous pouvez utiliser n'importe quel nom d'utilisateur.
* **Login :** ASSIA (ou votre nom)
* **Mot de passe :** (N'importe quoi, c'est une démo)

---

## ✨ Fonctionnalités Principales

* **Recherche Filtrée :** Par ville (Rabat, Tanger...), par genre (Filles/Garçons) et par budget.
* **Carte Interactive :** Visualisation des logements proches des universités (UM5, ENCG...).
* **Contact Direct :** Bouton WhatsApp intégré pour parler directement aux propriétaires ("Moul Dar").
* **Design Responsive :** L'interface s'adapte aux écrans (Laptop & Mobile).

---

*Projet réalisé dans le cadre du module Digital Creativity.*
