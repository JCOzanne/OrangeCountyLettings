Description des interfaces de programmation
===========================================

L’application ne propose pas d’API RESTful, mais s’appuie sur des vues Django classiques basées sur des routes URL. Ci-dessous la liste des principales interfaces accessibles via le navigateur ou des requêtes HTTP.

Vues principales
----------------

**Page d’accueil**

- **URL** : `/`
- **Méthode** : `GET`
- **Vue** : `oc_lettings_site.views.index`
- **Description** : Affiche la page d’accueil du site.
- **Retour** : HTML

**Lettings – Liste des locations**

- **URL** : `/lettings/`
- **Méthode** : `GET`
- **Vue** : `lettings.views.index`
- **Description** : Liste tous les biens immobiliers disponibles.
- **Retour** : HTML – Templating Django via `lettings/index.html`

**Lettings – Détail d’une location**

- **URL** : `/lettings/<int:letting_id>/`
- **Méthode** : `GET`
- **Vue** : `lettings.views.letting`
- **Paramètres** :
  - `letting_id` : ID du bien immobilier
- **Retour** : HTML – Templating Django via `lettings/letting.html`

**Profiles – Liste des utilisateurs**

- **URL** : `/profiles/`
- **Méthode** : `GET`
- **Vue** : `profiles.views.index`
- **Description** : Affiche la liste des profils utilisateurs.
- **Retour** : HTML – Templating Django via `profiles/index.html`

**Profiles – Détail d’un utilisateur**

- **URL** : `/profiles/<str:username>/`
- **Méthode** : `GET`
- **Vue** : `profiles.views.profile`
- **Paramètres** :
  - `username` : nom d’utilisateur Django
- **Retour** : HTML – Templating Django via `profiles/profile.html`

**Interface d’administration Django**

- **URL** : `/admin/`
- **Méthode** : `GET`
- **Description** : Interface standard d’administration Django. Connexion requise.
- **Accès** : réservé au superutilisateur

Modèle d'erreurs personnalisées
-------------------------------

L’application gère deux vues d’erreurs personnalisées :

- `404.html` → page non trouvée
- `500.html` → erreur serveur interne

Ces vues sont définies dans `oc_lettings_site.views` avec journalisation (`logging`) et capture via Sentry.

---