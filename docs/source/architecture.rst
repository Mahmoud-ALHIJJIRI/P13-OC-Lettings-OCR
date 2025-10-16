############
Architecture
############

Ce projet a été refactorisé d'une architecture monolithique vers une structure modulaire pour améliorer la maintenabilité et la séparation des responsabilités.

Structure des Applications
==========================

L'application est divisée en trois modules Django principaux :

* **oc_lettings_site**
  C'est le module principal du projet. Il gère la configuration globale (``settings.py``), le routage des URL de haut niveau (``urls.py``) et sert de point d'entrée pour le serveur WSGI.

* **lettings**
  Cette application est dédiée à la gestion des locations. Elle contient les modèles pour les adresses (``Address``) et les biens à louer (``Letting``), ainsi que les vues et les URL correspondantes.

* **profiles**
  Cette application gère les profils des utilisateurs. Elle contient le modèle ``Profile``, qui est lié au modèle ``User`` de Django, ainsi que les vues et les URL associées.
