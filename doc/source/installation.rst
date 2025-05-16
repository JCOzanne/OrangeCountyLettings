Installation
==================

Installation locale (environnement virtuel)
-------------------------------------------

1. Clonez le dépôt :
   ::

     git clone https://github.com/JCOzanne/OrangeCountyLettings.git
     cd OrangeCountyLettings

2. Créez un environnement virtuel et activez-le :
   ::

     python -m venv venv
     source venv/bin/activate      # Sous Linux/macOS
     venv\Scripts\activate         # Sous Windows

3. Installez les dépendances :
   ::

     pip install -r requirements.txt

4. Créez un fichier `.env` avec les variables suivantes :
   ::

     SECRET_KEY=your_secret_key
     DEBUG=True
     SENTRY_DSN=your_sentry_dsn

5. Lancez le serveur :
   ::

     python manage.py migrate
     python manage.py runserver

6. Accédez à l'application :
   Ouvrez votre navigateur à l'adresse : http://localhost:8000


Installation via Docker
------------------------

 ::

   # Prélables :

  - Avoir configuré son compte Docker Hub

  - Dans le dossier de votre choix, créer un fichier .env avec les variables suivantes :
  SECRET_KEY -> votre clé secrète Django
  (Vous pouvez en générer une en tapant la commande
  python -c 'import secrets; print(secrets.token_urlsafe(50))'
  dans votre terminal)
  DEBUG=True en développement, False en production
  SENTRY_DSN -> votre dsn Sentry

1. Extraire l'image Docker :
   ::

     docker pull jcozanne/orangecountylettings:latest.

2. Lancez le conteneur :
   ::

     docker run -p 8000:8000 --env-file .env jcozanne/orangecountylettings:latest

3. Accédez à l'application :
   Ouvrez votre navigateur à l'adresse : http://localhost:8000
