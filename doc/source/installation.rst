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

1. Construisez l'image Docker :
   ::

     docker build -t orangecountylettings .

2. Lancez le conteneur :
   ::

     docker run -p 8000:8000 orangecountylettings

3. Accédez à l'application :
   Ouvrez votre navigateur à l'adresse : http://localhost:8000
