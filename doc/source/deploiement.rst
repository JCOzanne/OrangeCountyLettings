Déploiement
===========

Ce chapitre décrit le processus de déploiement de l’application **Orange County Lettings**, incluant l’intégration continue (CI), la conteneurisation avec Docker, et la mise en production sur Render.


Configuration initiale
---------------------

Avant de commencer le déploiement, assurez-vous de disposer des éléments suivants :

1. Un compte GitHub avec votre dépôt configuré
2. Un compte Docker Hub pour stocker les images Docker
3. Un compte Render pour l'hébergement
4. Un compte Sentry pour la surveillance

Configuration de GitHub Actions
-----------------------------
Renseigner les secrets Github (github>settings>Secrets and variables>Actions)

   * ``DOCKER_USERNAME`` : Votre nom d'utilisateur Docker Hub
   * ``DOCKER_PASSWORD`` : Votre mot de passe Docker Hub
   * ``SECRET_KEY`` : Clé secrète Django
   * ``SENTRY_DSN`` : URL DSN de Sentry

Étapes de déploiement
----------------------

1. **CI/CD avec GitHub Actions**

Le projet utilise un pipeline CI/CD défini dans `.github/workflows/ci_cd.yml`.
Le comportement est le suivant :

- **Sur la branche `main` :**

  - Exécute les tests (`pytest`) et le linting (`flake8`)
  - Construit une image Docker (si les tests et le linting réussissent)
  - Pousse l’image vers Docker Hub avec deux tags :

    - `latest`
    - le hash du commit GitHub (`${{ github.sha }}`)

2. **Conteneurisation avec Docker**

L’application est entièrement contenue dans une image Docker :

- Le `Dockerfile` définit l’environnement Python, les dépendances et le serveur Gunicorn
- Les variables sensibles (`SECRET_KEY`, `SENTRY_DSN` et 'DEBUG') sont injectées au build via GitHub Secrets
- Les fichiers statiques sont collectés automatiquement au démarrage grâce à un script `start.sh`

Exemple de build local :

.. code-block:: bash

   docker build -t orangecountylettings .
   docker run -p 8000:8000 --env-file .env orangecountylettings

3. **Déploiement sur Render**

L’image Docker est utilisée sur [Render](https://render.com) pour la mise en production :

- Création d’un **Web Service** de type "Docker image"
- Image utilisée : `docker.io/<utilisateur>/orangecountylettings:latest`
- Port exposé : `8000`
- Variables d’environnement : définies dans Render (SECRET_KEY, DEBUG, SENTRY_DSN, etc.)
- Commande de démarrage personnalisée : `./start.sh`

4. **Gestion des fichiers statiques**

- Les fichiers statiques sont collectés dynamiquement avec `collectstatic`
- **Whitenoise** est utilisé pour les servir en production
- `STATIC_ROOT` est défini dans `settings.py` comme `BASE_DIR / "staticfiles"`

5. **Sécurité et bonnes pratiques**

- `DEBUG=False` en production
- `ALLOWED_HOSTS` est dynamique avec la variable `RENDER_EXTERNAL_HOSTNAME`
- Aucune variable sensible n’est exposée (tout passe par `.env` ou secrets GitHub)

6. **Déploiement manuel (Render)**

Sur Render, assurez-vous que :

- Le mode de déploiement automatique est **désactivé**
- Le bouton **Manual Deploy** est utilisé uniquement après validation du pipeline CI

Reproduire le déploiement localement
-------------------------------------

Une image Docker peut être récupérée depuis Docker Hub puis lancée sans le code source :

.. code-block:: bash

   docker pull <utilisateur>/orangecountylettings:latest
   docker run -p 8000:8000  <utilisateur>/orangecountylettings:latest
