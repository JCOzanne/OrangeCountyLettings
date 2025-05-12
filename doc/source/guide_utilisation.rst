Guide d’utilisation
====================

Ce guide vous explique comment utiliser l’application Orange County Lettings, avec des cas d'utilisation.

Navigation générale
-------------------

L’interface est simple, la navigation se fait via les boutons 'Profiles' et 'settings'. Voici les principales sections de l’application :

Page d’accueil
^^^^^^^^^^^^^^

La page d’accueil est accessible à l’URL racine (/). Elle présente :

- Un message de bienvenue
- Des liens vers les sections "Lettings" et "Profiles"

.. image:: doc/source/_static/home_page.png
   :alt: Capture d’écran de la page d’accueil
   :align: center
   :width: 80%

Section Lettings
^^^^^^^^^^^^^^^^

Accessible via `/lettings/`, cette section présente la liste des biens disponibles à la location.

*Cas d’utilisation 1 – Consulter tous les biens :*
- Accédez à la page d’accueil
- Cliquez sur "Lettings"
- Parcourez la liste des biens disponibles

*Cas d’utilisation 2 – Voir les détails d’un bien :*
- Depuis la liste, cliquez sur un titre
- Consultez les détails (nom et adresse)

Section Profiles
^^^^^^^^^^^^^^^^

Accessible via `/profiles/`, cette section affiche tous les profils utilisateurs.

*Cas d’utilisation 3 – Voir tous les profils :*
- Depuis la page d’accueil, cliquez sur "Profiles"
- Parcourez les profils

*Cas d’utilisation 4 – Voir un profil :*
- Cliquez sur un nom d’utilisateur
- Consultez sa ville favorite

Administration
--------------

L’administration du site est disponible via `/admin/`.

*Cas d’utilisation 5 – Accéder à l’interface d’administration :*
- Rendez-vous sur `/admin/`
- Connectez-vous avec vos identifiants admin
- Gérer les données via l’interface Django Admin

Bonnes pratiques et dépannage
-----------------------------

- Utilisez le lien "Home" pour revenir à l’accueil
- URLs logiques et prévisibles :
  - `/lettings/` → tous les biens
  - `/profiles/` → tous les profils

Problèmes courants :

- **Erreur 404** : URL incorrecte ou ressource absente
- **Erreur 500** : erreur interne (journalisée via Sentry)
- **Problèmes d’affichage** : vider le cache du navigateur
