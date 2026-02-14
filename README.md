# 🚗 AutoCameroun - Application Web de Vente de Voitures

**AutoCameroun** est une plateforme web moderne et intuitive de mise en relation entre acheteurs et vendeurs de véhicules au Cameroun. Développée avec **Django** et **MySQL**, elle offre une expérience utilisateur premium inspirée des standards internationaux de l'e-commerce automobile.

---

## 🌟 Fonctionnalités Clés

### 👤 Gestion des Utilisateurs
- **Inscription & Connexion** : Rôles différenciés pour les **Acheteurs** et les **Vendeurs**.
- **Sécurité** : Protection des accès et gestion des profils (noms camerounais supportés).

### 🚘 Catalogue Automobile
- **Recherche Avancée** : Filtrage par marque, prix (en FCFA), type de carburant et année.
- **Fiches Détaillées** : Galeries photos, caractéristiques techniques complètes et descriptions.
- **Mise en Vente** : Formulaire de dépôt d'annonce avec **prévisualisation d'images en temps réel**.

### 💬 Communication & Transactions
- **Messagerie Interne** : Système de chat direct entre l'acheteur et le vendeur pour chaque annonce.
- **Réservations** : Possibilité de réserver ou commander un véhicule en un clic.

### 🛡️ Administration & Modération
- **Validation des Annonces** : Les annonces doivent être approuvées par un administrateur avant d'être publiques.
- **Dashboards dédiés** : Tableaux de bord pour les vendeurs (suivi des ventes) et les administrateurs (gestion du catalogue).

---

## 🛠️ Stack Technique

- **Framework Backend** : Python Django 5.x
- **Base de données** : MySQL / MariaDB
- **Frontend** : HTML5, CSS3 (Custom), JavaScript (Vanilla)
- **Framework CSS** : Bootstrap 5.3 + FontAwesome 6
- **Traitement d'images** : Pillow

---

## 🚀 Installation Locale

### 1. Cloner le projet & Préparer l'environnement
```bash
git clone <url-du-repo>
cd ICT205/TP
python -m venv venv
source venv/bin/activate  # Sur Linux/Mac
pip install -r requirements.txt
```

### 2. Configuration de la Base de Données (MySQL)

L'application est configurée pour utiliser un utilisateur dédié par sécurité. Suivez ces étapes :

1.  **Connectez-vous à MySQL** en tant que root :
    ```bash
    mysql -u root -p
    ```
2.  **Exécutez les commandes suivantes** pour créer la base et l'utilisateur :
    ```sql
    CREATE DATABASE car_sales_db CHARACTER SET utf8mb4;
    CREATE USER 'car_user'@'127.0.0.1' IDENTIFIED BY 'CarPass123!';
    GRANT ALL PRIVILEGES ON car_sales_db.* TO 'car_user'@'127.0.0.1';
    FLUSH PRIVILEGES;
    EXIT;
    ```

### 3. Initialisation et Peuplage (Données Camerounaises)

Une fois la base de données prête, appliquez les migrations et remplissez-la avec des données de test :

1.  **Appliquer les migrations** :
    ```bash
    python manage.py migrate
    ```
2.  **Peupler la base de données** (Ajout de vendeurs, acheteurs et voitures locales) :
    ```bash
    python seed_data.py
    ```
    *Note : Tous les utilisateurs créés par ce script (ekotto, abena, etc.) ont pour mot de passe : `pass1234`.*

3.  **Créer un compte Administrateur** (pour valider les annonces) :
    ```bash
    python manage.py createsuperuser
    ```

### 4. Lancer le serveur
```bash
python manage.py runserver
```

---

## 📂 Structure du Projet
- `car_sales/` : Configuration globale du projet Django.
- `cars/` : Application principale (Modèles, Vues, Logique métier).
- `static/` : Fichiers CSS personnalisés et images.
- `templates/` : Architecture des pages HTML (Base, Enregistrement, Voitures).
- `seed_data.py` : Script pour peupler la base avec des noms camerounais et des données de test.

---

## ✍️ Auteur
Projet réalisé dans le cadre du module **ICT205 - Développement Web**.
Date : Février 2026
Localisation : Douala, Cameroun