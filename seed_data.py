import os
import django
import random

# Configuration de l'environnement Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_sales.settings')
django.setup()

from django.contrib.auth.models import User
from cars.models import Profile, Car, Message, CarImage

def run_seed():
    print("Début du peuplage de la base de données...")

    # 1. Création des utilisateurs (Noms Camerounais)
    users_data = [
        {'username': 'ekotto', 'first_name': 'Jean', 'last_name': 'Ekotto', 'role': 'seller'},
        {'username': 'nguemo', 'first_name': 'Samuel', 'last_name': 'Nguemo', 'role': 'seller'},
        {'username': 'abena', 'first_name': 'Marie', 'last_name': 'Abena', 'role': 'buyer'},
        {'username': 'fotsing', 'first_name': 'Hervé', 'last_name': 'Fotsing', 'role': 'buyer'},
        {'username': 'nda_voundi', 'first_name': 'Cécile', 'last_name': 'Nda Voundi', 'role': 'seller'},
    ]

    users = []
    for data in users_data:
        user, created = User.objects.get_or_create(
            username=data['username'],
            defaults={'first_name': data['first_name'], 'last_name': data['last_name']}
        )
        if created:
            user.set_password('pass1234')
            user.save()
            Profile.objects.get_or_create(user=user, defaults={'role': data['role']})
            print(f"Utilisateur créé : {user.username}")
        users.append(user)

    # 2. Création de voitures
    cars_data = [
        {'brand': 'Toyota', 'model': 'Avensis', 'year': 2012, 'price': 4500000, 'mileage': 150000, 'fuel': 'diesel', 'seller': users[0]},
        {'brand': 'Mercedes', 'model': 'C-Class', 'year': 2015, 'price': 8000000, 'mileage': 95000, 'fuel': 'gasoline', 'seller': users[1]},
        {'brand': 'Hyundai', 'model': 'Santa Fe', 'year': 2018, 'price': 12000000, 'mileage': 45000, 'fuel': 'diesel', 'seller': users[4]},
        {'brand': 'Suzuki', 'model': 'Vitara', 'year': 2020, 'price': 15500000, 'mileage': 12000, 'fuel': 'gasoline', 'seller': users[0]},
    ]

    cars = []
    for data in cars_data:
        car, created = Car.objects.get_or_create(
            brand=data['brand'],
            model=data['model'],
            seller=data['seller'],
            defaults={
                'year': data['year'],
                'price': data['price'],
                'mileage': data['mileage'],
                'fuel_type': data['fuel'],
                'description': f"Très belle {data['brand']} bien entretenue à Douala.",
                'is_validated': True # Directement validées pour le test
            }
        )
        if created:
            print(f"Voiture ajoutée : {car.brand} {car.model}")
        cars.append(car)

    # 3. Création de quelques messages
    messages_content = [
        "Bonjour, est-ce que le prix est discutable ?",
        "Je suis intéressé, peut-on se voir à Bastos pour le test ?",
        "Le moteur a-t-il déjà été ouvert ?",
        "Est-ce que vous acceptez un paiement en deux tranches ?"
    ]

    for i in range(5):
        sender = random.choice([users[2], users[3]]) # Les acheteurs
        car = random.choice(cars)
        Message.objects.create(
            sender=sender,
            receiver=car.seller,
            car=car,
            content=random.choice(messages_content)
        )
    
    print("Peuplage terminé avec succès !")

if __name__ == "__main__":
    run_seed()
