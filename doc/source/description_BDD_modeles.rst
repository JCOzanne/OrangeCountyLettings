Structure de la base de données et des modèles
==========================================

Vue d'ensemble
--------------

Orange County Lettings utilise une base de données SQLite pour stocker les informations sur les biens immobiliers et les profils utilisateurs. L’architecture est divisée entre les applications `lettings` et `profiles`.

Schéma simplifié
----------------

::

    +-------------------+       +-------------------+       +-------------------+
    |      Address      |       |      Letting      |       |      Profile      |
    +-------------------+       +-------------------+       +-------------------+
    | id (PK)           |       | id (PK)           |       | id (PK)           |
    | number            |<------| address (FK)      |       | user (FK)         |
    | street            |       | title             |       | favorite_city     |
    | city              |       |                   |       |                   |
    | state             |       |                   |       |                   |
    | zip_code          |       |                   |       |                   |
    | country_iso_code  |       |                   |       |                   |
    +-------------------+       +-------------------+       +-------------------+
                                                                      |
                                                                      v
                                                            +-------------------+
                                                            |       User        |
                                                            +-------------------+
                                                            | id (PK)           |
                                                            | username          |
                                                            | password          |
                                                            | email             |
                                                            +-------------------+

Modèles détaillés
-----------------

**Application `lettings`**

*Modèle Address* ::

    class Address(models.Model):
        number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
        street = models.CharField(max_length=64)
        city = models.CharField(max_length=64)
        state = models.CharField(max_length=2)
        zip_code = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
        country_iso_code = models.CharField(max_length=3)

        def __str__(self):
            return f'{self.number} {self.street}'

        class Meta:
            verbose_name_plural = "Addresses"

*Modèle Letting* ::

    class Letting(models.Model):
        title = models.CharField(max_length=256)
        address = models.OneToOneField(Address, on_delete=models.CASCADE)

        def __str__(self):
            return self.title

**Application `profiles`**

*Modèle Profile* ::

    class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        favorite_city = models.CharField(max_length=64, blank=True)

        def __str__(self):
            return self.user.username

Relations entre les modèles
----------------------------

- `Letting` → `Address` : relation OneToOne (un logement = une adresse unique)
- `Profile` → `User` : relation OneToOne (un profil utilisateur = un compte )

Migrations
----------

Créer les migrations :

.. code-block:: bash

    python manage.py makemigrations

Appliquer les migrations :

.. code-block:: bash

    python manage.py migrate

Exemples avec l’ORM
--------------------

.. code-block:: python

     Récupérer tous les biens locatifs
    lettings = Letting.objects.all()

     Récupérer un bien spécifique par ID
    letting = Letting.objects.get(id=1)

     Récupérer tous les profils
    profiles = Profile.objects.all()

     Récupérer un profil par nom d'utilisateur
    profile = Profile.objects.get(user__username='username')

---
