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
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
# Ou manuellement :
pip install django mysqlclient Pillow pymysql
```

### 3. Configurer la base de données
1. Créez une base de données MySQL nommée `car_sales_db`.
2. Créez un utilisateur `car_user` avec le mot de passe `CarPass123!`.
3. Donnez-lui les droits sur la base : `GRANT ALL PRIVILEGES ON car_sales_db.* TO 'car_user'@'127.0.0.1';`.

### 4. Lancer les migrations & le serveur
```bash
python manage.py migrate
python manage.py createsuperuser  # Pour accéder au panel admin
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