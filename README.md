# projet_facture
# Application Django – Générateur de Factures

Ce projet est une application web développée avec Django. Elle permet de gérer une liste de produits et de générer des factures associées. Chaque facture peut contenir plusieurs produits avec des quantités précises. L’objectif était de mettre en place une interface simple, claire et fonctionnelle pour répondre à un besoin de gestion commerciale de base.

## Fonctionnalités

- Création, modification et suppression de produits.
- Génération de factures avec sélection de plusieurs produits et définition des quantités.
- Affichage des détails d’une facture (liste des produits, sous-totaux, total global).
- Pagination sur les listes de produits et de factures.
- Interface utilisateur responsive avec Bootstrap.

## Technologies utilisées

- Python 3
- Django (framework web)
- SQLite (base de données par défaut)
- HTML, CSS (via Bootstrap 5)

## Installation

1. Cloner ce dépôt :
   git clone https://github.com/votre-utilisateur/generateur-facture.git
   cd generateur-facture
2. Installer les dépendances :
    pip install django
3. Appliquer les migrations :
    python manage.py migrate
4. Lancer le serveur :
    python manage.py runserver
5. Accéder à l’application via http://127.0.0.1:8000/
