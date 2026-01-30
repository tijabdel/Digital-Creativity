# 🏠 StudentHouse

**Projet réalisé dans le cadre du module Digital Creativity.**

## 📋 Présentation
**StudentHouse** est une plateforme web conçue pour simplifier la recherche de logement pour les étudiants marocains.

Notre objectif était de proposer une alternative fiable aux groupes Facebook et aux sites généralistes (Avito), en ciblant spécifiquement les besoins étudiants : proximité des facultés (ENCG, FST, UM5...), budget adapté et critères de colocation.

L'accent a été mis sur **l'expérience utilisateur (UX)** avec un design "Light Mode" épuré et une interactivité fluide.

---

## 👥 L'Équipe
Ce projet a été développé par notre groupe de 4 membres :

* **Membre 1** (Assia Belaissia)
* **Membre 2**
* **Membre 3**
* **Membre 4**

---

## ⚙️ Installation Technique

Le projet est construit avec **Django** (Python). Voici la procédure pour le lancer sur votre machine :

### 1. Configuration de l'environnement
Ouvrez le terminal dans le dossier du projet :

\\\ash
# Activer l'environnement virtuel
.\venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
\\\

### 2. Initialisation des Données (Important)
Nous avons développé un script d'automatisation pour pré-remplir la base de données avec des résidences réelles (Bayt Al Maârifa, Ziraoui...) afin de rendre la démo pertinente.

\\\ash
# Créer les tables et injecter les données
python manage.py makemigrations housing
python manage.py migrate
python seed.py
\\\

### 3. Lancement
\\\ash
python manage.py runserver
\\\
Accès : **http://127.0.0.1:8000/**

---

## 💡 Fonctionnalités Clés

Nous avons intégré plusieurs fonctionnalités spécifiques au contexte marocain :

1.  **Filtrage Contextuel :**
    * Possibilité de filtrer par **Genre** (Filles / Garçons), un critère essentiel pour les résidences et colocations au Maroc.
    * Filtres dynamiques par Ville et Budget.

2.  **Cartographie Interactive :**
    * Utilisation de *Leaflet.js* (léger et rapide).
    * **Code couleur :** Les résidences vérifiées apparaissent en Bleu, les annonces particulières en Violet.

3.  **Système "Moul Dar" (Bailleurs) :**
    * Tout utilisateur peut publier une annonce via son Espace Personnel.
    * Intégration d'un bouton **WhatsApp API** pour contacter directement le propriétaire sans intermédiaire.

---

*Génie des Systèmes et Réseaux - ENSA*
