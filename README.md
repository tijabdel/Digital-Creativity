# 🏠 StudentHouse (Projet de Groupe)

**Module : Digital Creativity**

Bonjour ! Voici le rendu final de notre projet **StudentHouse**.

Nous sommes une équipe de 4 étudiants et nous avons voulu créer une solution concrète pour le logement étudiant au Maroc.
Le but est simple : remplacer les fichiers Excel et les groupes Facebook par une vraie plateforme, fiable et moderne.

---

## 👥 L'Équipe Projet

* **Membre 1** : (Mets ton nom ici - ex: Assia Belaissia)
* **Membre 2** : (Nom du collègue)
* **Membre 3** : (Nom du collègue)
* **Membre 4** : (Nom du collègue)

---

## 💡 Pourquoi ce projet ?

Nous sommes partis d'un constat réel : trouver un logement près de son école (ENCG, FST, UM5...) est souvent un calvaire.
Nous avons donc conçu une application qui mise tout sur le **réalisme** et l'**interactivité**.

### Nos fonctionnalités clés :
1.  **Données Réelles & Vérifiées** :
    * Nous avons intégré les vrais prix et localisations des résidences (ex: *Bayt Al Maârifa*, *Résidence Ziraoui*).
    * Les logements vérifiés ont un badge spécial sur la carte.

2.  **Interactivité Totale (Style "Moul Dar")** :
    * L'application permet aux utilisateurs de **publier leur propre annonce**.
    * Si vous libérez votre chambre, vous pouvez l'ajouter via l'espace "Publier".

3.  **Communication Directe** :
    * Pas de formulaires inutiles : un bouton **WhatsApp** ouvre directement la discussion avec le propriétaire.

4.  **Design "Light Mode"** :
    * Nous avons opté pour une interface épurée (style Airbnb) pour que l'information soit lisible et accessible.

---

## 🔧 Guide d'Installation (Pour le correcteur)

Le projet tourne sous Python/Django. Voici comment le lancer chez vous en 3 étapes :

### 1. Préparer l'environnement
\\\ash
# Dans le dossier du projet :
.\venv\Scripts\activate
pip install -r requirements.txt
\\\

### 2. Charger les données (Important)
Nous avons créé un script spécial pour ne pas livrer une coquille vide.
Lancez ceci pour remplir le site avec nos exemples réels :
\\\ash
python manage.py makemigrations housing
python manage.py migrate
python seed.py
\\\

### 3. Lancer le site
\\\ash
python manage.py runserver
\\\
👉 **http://127.0.0.1:8000/**

---

## 📍 Ce qu'il faut tester
* Connectez-vous (pseudo libre).
* Allez sur la **Carte** pour voir la différence entre les résidences privées (Bleu) et les particuliers (Violet).
* Essayez les **Filtres** (notamment le filtre "Filles/Garçons", très important au Maroc).

Merci de nous lire !
