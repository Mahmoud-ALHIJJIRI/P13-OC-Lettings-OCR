############
Architecture
############

Ce projet a été refactorisé d'une architecture monolithique vers une structure **modulaire**,
afin d'améliorer la maintenabilité, la lisibilité du code et la séparation des responsabilités.

==============================
Structure générale du projet
==============================

Le projet Django est désormais organisé en **trois applications principales** :

* **oc_lettings_site**
  Gère la configuration globale du projet.
  Ce module contient :

  - Le fichier de configuration principale (``settings.py``)
  - Le routage des URL de haut niveau (``urls.py``)
  - Le point d'entrée WSGI/ASGI

  Il sert de "cœur" du projet et délègue la logique métier aux applications dédiées.

* **lettings**
  Application dédiée à la gestion des locations.
  Elle contient :

  - Les modèles ``Address`` et ``Letting``
  - Les vues associées (liste, détail, etc.)
  - Les fichiers de templates dans ``lettings/templates/lettings/``
  - Les URLs avec un espace de noms (namespace) ``lettings``

  Cette application gère tout ce qui concerne les biens immobiliers et leurs adresses.

* **profiles**
  Application responsable de la gestion des profils utilisateurs.
  Elle contient :

  - Le modèle ``Profile``, lié au modèle ``User`` natif de Django (relation OneToOne)
  - Les vues et templates associés dans ``profiles/templates/profiles/``
  - Les URLs avec un namespace ``profiles``

  Elle permet d’afficher et de gérer les profils utilisateurs du site.

==============================
Objectifs du refactoring
==============================

- **Séparation des responsabilités** : chaque domaine fonctionnel dispose désormais de son propre module.
- **Meilleure maintenabilité** : le code est plus clair et plus facile à tester.
- **Évolutivité** : l’architecture facilite l’ajout de nouvelles fonctionnalités sans impacter le cœur du site.
- **Lisibilité** : les templates et vues sont mieux organisés par application.

==============================
Structure du répertoire
==============================

::

    oc_lettings_site/
        settings.py
        urls.py
        wsgi.py
        asgi.py
    lettings/
        models.py
        views.py
        urls.py
        templates/
            lettings/
                index.html
                letting.html
    profiles/
        models.py
        views.py
        urls.py
        templates/
            profiles/
                index.html
                profile.html
    templates/
        404.html
        500.html
    manage.py

==============================
Routage et namespaces
==============================

Le fichier ``oc_lettings_site/urls.py`` inclut désormais les URL des applications avec leurs namespaces respectifs :

.. code-block:: python

    from django.urls import include, path

    urlpatterns = [
        path('', include('lettings.urls', namespace='lettings')),
        path('profiles/', include('profiles.urls', namespace='profiles')),
    ]

Chaque application définit son propre ``urls.py`` avec la variable ``app_name`` pour isoler les routes :

.. code-block:: python

    # lettings/urls.py
    from django.urls import path
    from . import views

    app_name = 'lettings'

    urlpatterns = [
        path('', views.index, name='index'),
        path('<int:letting_id>/', views.letting, name='letting'),
    ]

==============================
Templates et cohérence visuelle
==============================

Les templates ont été réorganisés dans leurs répertoires respectifs tout en **préservant l’apparence et le comportement existants**.

Exemples :
- ``lettings_index.html`` → ``lettings/templates/lettings/index.html``
- ``profiles_index.html`` → ``profiles/templates/profiles/index.html``

Les vues correspondantes ont été renommées en conséquence :
- ``lettings_index`` → ``index``
- ``profiles_index`` → ``index``

==============================
Améliorations supplémentaires
==============================

- **Pluralisation corrigée** :
  Le modèle ``Address`` affichait à tort « Addresss » dans l’interface d’administration.
  Cela a été corrigé grâce à l’ajout de :

  .. code-block:: python

      class Meta:
          verbose_name_plural = "addresses"

- **Pages d’erreur personnalisées (404 et 500)** :
  Des templates dédiés ``404.html`` et ``500.html`` ont été créés pour améliorer l’expérience utilisateur.
  Les handlers sont définis dans ``oc_lettings_site/urls.py`` :

  .. code-block:: python

      handler404 = 'oc_lettings_site.views.custom_404'
      handler500 = 'oc_lettings_site.views.custom_500'

==============================
Qualité du code et tests
==============================

- **Linter** : toutes les erreurs détectées par ``flake8`` ont été corrigées sans modifier la configuration.
- **Documentation** : chaque module, classe et fonction contient désormais une docstring claire et descriptive.
- **Tests unitaires et d’intégration** :
  - Couvrent les modèles, vues et URLs.
  - Répartis par application.
  - Objectif : **couverture de code ≥ 80%**.

==============================
Conclusion
==============================

Cette refonte modulaire rend le projet plus clair, plus robuste et prêt à évoluer.
L’apparence et le fonctionnement du site restent inchangés pour l’utilisateur final,
tandis que la structure interne est désormais alignée sur les bonnes pratiques Django.
