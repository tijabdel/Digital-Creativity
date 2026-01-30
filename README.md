# 🏠 StudentHouse (Projet Digital Creativity)

Bonjour ! Voici le rendu final de mon projet **StudentHouse**.

L'idée était de créer une plateforme qui aide vraiment les étudiants marocains à trouver un logement, sans tomber sur des arnaques. J'ai voulu faire quelque chose de plus "propre" et moderne que les sites qu'on utilise d'habitude (comme Avito ou les groupes Facebook).

J'ai passé beaucoup de temps sur le design (Mode Clair / Minimaliste) et sur l'interactivité.

---

## 🔧 Comment tester le projet sur votre machine

J'ai essayé de rendre l'installation la plus simple possible. Il vous faut juste **Python**.

### 1. Installation

Ouvrez le dossier dans le terminal et lancez ces commandes une par une :

**Activer l'environnement virtuel (pour ne pas mélanger les bibliothèques) :**
\\\ash
.\venv\Scripts\activate
\\\

**Installer ce qu'il faut (Django, etc.) :**
\\\ash
pip install -r requirements.txt
\\\

### 2. La Base de Données (Important !)

Au lieu de vous laisser devant une application vide, j'ai codé un petit script spécial (seed.py) qui remplit le site avec des **vraies données**.
Il va ajouter automatiquement des résidences comme *Bayt Al Maârifa* ou *Ziraoui* avec les vrais prix du marché.

Lancez simplement :
\\\ash
python manage.py makemigrations housing
python manage.py migrate
python seed.py
\\\
*(Si vous voyez "7 Annonces Réalistes Importées", c'est que c'est bon !)*

### 3. Lancer le site

\\\ash
python manage.py runserver
\\\
Ensuite, cliquez ici : **http://127.0.0.1:8000/**

---

## 💡 Ce qu'il faut tester

Une fois sur le site, voici les fonctionnalités principales que j'ai développées :

1.  **La Carte Interactive :** Elle n'utilise pas Google Maps (trop lourd), mais *Leaflet*. J'ai mis des marqueurs de couleurs différentes :
    * 🔵 **Bleu :** Les résidences universitaires vérifiées.
    * 🟣 **Violet :** Les annonces des particuliers.

2.  **Publier une annonce :** Connectez-vous (Pseudo : "Assia" ou ce que vous voulez) et allez dans **"Mon Espace"**. Vous verrez un bouton pour ajouter votre propre annonce. Elle apparaîtra directement sur la carte !

3.  **Le contact WhatsApp :** Sur chaque annonce, le bouton "Contacter" ouvre vraiment une discussion WhatsApp (simulée avec un numéro marocain).

4.  **Les Filtres :** Vous pouvez trier par ville, budget, mais surtout par **Genre** (Filles / Garçons), car c'est un critère essentiel au Maroc que beaucoup d'applis oublient.

---

Merci d'avoir pris le temps de tester !
Si vous avez un souci pour lancer le serveur, n'hésitez pas à me le dire.

**Assia**
*Génie des Systèmes et Réseaux - ENSA*
