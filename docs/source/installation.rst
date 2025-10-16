###################
Installation Locale
###################

Ce guide vous explique comment installer et lancer le projet sur votre machine locale pour le développement.

Prérequis
=========
* Python 3.11 ou supérieur
* Git

Étapes d'installation
=====================

1. **Clonez le dépôt**
   Ouvrez un terminal et clonez le dépôt depuis GitHub :

   .. code-block:: bash

      git clone https://github.com/SalehTrissi/Python-OC-Lettings-FR.git
      cd Python-OC-Lettings-FR

2. **Créez et activez l'environnement virtuel**
   Il est fortement recommandé d'utiliser un environnement virtuel.

   .. code-block:: bash

      python -m venv venv

   * **Sur macOS/Linux :** ``source venv/bin/activate``
   * **Sur Windows (PowerShell) :** ``.\venv\Scripts\Activate.ps1``

   .. note::
      Si vous rencontrez une erreur de sécurité sur Windows, ouvrez PowerShell en tant qu'administrateur et exécutez la commande ``Set-ExecutionPolicy RemoteSigned``.

3. **Installez les dépendances**

   .. code-block:: bash

      pip install -r requirements.txt

4. **Appliquez les migrations**

   .. code-block:: bash

      python manage.py migrate

Lancer le Serveur
=================

* **Mode Développement (Recommandé)**
  Ouvrez le fichier ``oc_lettings_site/settings.py``, assurez-vous que ``DEBUG = True``, puis lancez :

  .. code-block:: bash

     python manage.py runserver

* **Mode Production Locale**
  Ce mode est utile pour tester les pages d'erreur personnalisées. Dans ``settings.py``, passez ``DEBUG`` à ``False``, puis exécutez :

  .. code-block:: bash

     python manage.py collectstatic --noinput
     python manage.py runserver

Le site est maintenant accessible à l'adresse http://127.0.0.1:8000.

Accès à l'Interface d'Administration
====================================
L'interface d'administration est disponible à l'adresse http://127.0.0.1:8000/admin.

* **Utilisateur par défaut :** ``admin``
* **Mot de passe :** ``Abc1234!``

Pour créer votre propre administrateur, utilisez la commande :

   .. code-block:: bash

      python manage.py createsuperuser