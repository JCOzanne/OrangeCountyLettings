Guide de démarrage rapide
==========================

Ce guide vous permettra de mettre en route l'application **Orange County Lettings** rapidement.

Prérequis : avoir un compte Sentry et un dsn sentry


1. **Installation rapide**
   ::

     # Cloner le dépôt
     git clone https://github.com/JCOzanne/OrangeCountyLettings.git
     cd OrangeCountyLettings

     # Créer et activer l'environnement virtuel
     python -m venv venv
     source venv/bin/activate       # ou venv\Scripts\activate sous Windows

     # Installer les dépendances
     pip install -r requirements.txt

     # Configurer l'environnement : créer un fichier .env avec les variables suivantes
     SECRET_KEY -> votre clé secrète Django
     (Vous pouvez en générer une en tapant la commande
     python -c 'import secrets; print(secrets.token_urlsafe(50))'
     dans votre terminal)
     DEBUG=True en développement, False en production
     SENTRY_DSN -> votre dsn Sentry

     # Appliquer les migrations
     python manage.py migrate

2. **Démarrer le serveur de développement**
   ::

     python manage.py runserver

   L'application est maintenant accessible à l'adresse : http://127.0.0.1:8000/


Structure de l'application
--------------------------

Le projet est composé de **trois modules principaux** :

- ``oc_lettings_site`` : module principal contenant la configuration du projet Django ;
- ``lettings`` : gestion des biens immobiliers disponibles à la location ;
- ``profiles`` : gestion des profils utilisateurs.

Pages principales
-----------------

+---------------------------+----------------------------------------------------------+
| URL                       | Description                                              |
+===========================+==========================================================+
| ``/``                     | Page d'accueil                                           |
+---------------------------+----------------------------------------------------------+
| ``/lettings/``            | Liste des biens disponibles                              |
+---------------------------+----------------------------------------------------------+
| ``/lettings/<id>/``       | Détail d’un bien spécifique                              |
+---------------------------+----------------------------------------------------------+
| ``/profiles/``            | Liste des profils utilisateurs                           |
+---------------------------+----------------------------------------------------------+
| ``/profiles/<username>/`` | Détail d’un profil utilisateur                           |
+---------------------------+----------------------------------------------------------+
| ``/admin/``               | Interface d’administration (connexion admin requise)     |
+---------------------------+----------------------------------------------------------+


Installation avec Docker
-----------------------

Pour un démarrage rapide avec **Docker** :

 ::

  # Préalables

  - docker installé sur sa machine

  - Dans le dossier de votre choix, créer un fichier .env avec les variables suivantes :
  SECRET_KEY -> votre clé secrète Django
  (Vous pouvez en générer une en tapant la commande
  python -c 'import secrets; print(secrets.token_urlsafe(50))'
  dans votre terminal)
  DEBUG=True en développement, False en production
  SENTRY_DSN -> votre dsn Sentry

  # Extraire et exécuter l'image Docker

  docker pull jcozanne/orangecountylettings:latest
  docker run -p 8000:8000 --env-file .env jcozanne/orangecountylettings:latest


L'application sera accessible à l'adresse : http://127.0.0.1:8000/
