# Orange County Lettings

[![CI/CD Pipeline](https://github.com/SalehTrissi/Python-OC-Lettings-FR/actions/workflows/main.yml/badge.svg)](https://github.com/SalehTrissi/Python-OC-Lettings-FR/actions)
[![Documentation Status](https://readthedocs.org/projects/trissi-mohammad-saleh-python-oc-lettings-fr/badge/?version=latest)](https://trissi-mohammad-saleh-python-oc-lettings-fr.readthedocs.io/fr/latest/?badge=latest)

Ce projet est une application web Django pour la gestion de locations immobilières. Il a fait l'objet d'une refactorisation d'une architecture monolithique vers une structure modulaire, avec l'intégration d'un pipeline CI/CD complet.

---

## Stack Technique

* **Backend :** Python, Django
* **Base de Données :** SQLite3
* **Tests :** Pytest, Coverage.py
* **Qualité de Code :** Flake8
* **CI/CD :** GitHub Actions
* **Conteneurisation :** Docker
* **Hébergement :** Render
* **Monitoring :** Sentry
* **Documentation :** Sphinx, Read the Docs

---

## Installation Locale

Suivez ces étapes pour configurer et lancer le projet sur votre machine.

### 1. Prérequis

* Python (version 3.9 ou supérieure)
* Git

### 2. Guide d'Installation

1. **Cloner le Dépôt**

    ```bash
    git clone https://github.com/Mahmoud-ALHIJJIRI/P13-OC-Lettings-OCR.git
    ```

2. **Naviguer dans le Dossier du Projet**
    Toutes les commandes suivantes doivent être exécutées depuis la racine du projet.

    ```bash
    cd P13-OC-Lettings--OCR
    ```

3. **Créer et Activer l'Environnement Virtuel**

    ```bash
    python -m venv env
    ```

    * **macOS/Linux :** `source env/bin/activate`
    * **Windows (PowerShell) :** `.\env\Scripts\activate`

4. **Installer les Dépendances**

    ```bash
    pip install -r requirements.txt
    ```

5. **Configurer les Variables d'Environnement (pour Sentry)**
    Pour le monitoring des erreurs, créez un fichier `.env` à la racine du projet et ajoutez uniquement votre clé Sentry :

    ```env
    # Clé DSN pour le monitoring avec Sentry
    SENTRY_DSN=https://votre_cle_sentry@...
    SECRET_KEY=secret_key_example
    ENVIROMENT=development
    ```

6. **Initialiser la Base de Données**

    ```bash
    python manage.py migrate
    ```

---

## Utilisation Locale

### Lancer le Serveur

* **Mode Développement (Recommandé)** :
    Ouvrez `oc_lettings_site/settings.py`, assurez-vous que `DEBUG = True` et lancez :

    ```bash
    python manage.py runserver
    ```

* **Mode Production Locale** (pour tester les pages d'erreur 404/500) :
    Dans `oc_lettings_site/settings.py`, passez `DEBUG` à `False`, puis exécutez dans le terminal :

    ```bash
    python manage.py collectstatic
    python manage.py runserver
    ```

### Lancer le Serveur avec Docker

Cette méthode permet de lancer l'application dans un environnement conteneurisé, identique à celui utilisé par le pipeline CI/CD.

1. **Prérequis :** Assurez-vous que Docker Desktop est installé et en cours d'exécution.
2. **Construire l'image Docker :**
    Cette commande lit le `Dockerfile` et construit l'image de votre application.

    ```bash
    docker-compose build
    ```

3. **Démarrer le conteneur :**
    Cette commande démarre l'application à partir de l'image construite. Vous verrez les logs du serveur s'afficher dans votre terminal.

    ```bash
    docker pull malhijjiri/oc-lettings-site:latest
    ```

    Pour commencer le service.

    ```bash
    docker build -t oc-lettings-site
    ```
   Executer le container
    ```bash
   docker run -p 8000:8000 oc-lettings-site 
   ```

---

Le site est accessible à l'adresse [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Outils de Qualité et Tests

* **Lancer les tests et voir la couverture :**

    ```bash
    pytest
    ```

* **Vérifier la qualité du code (Linting) :**

    ```bash
    flake8
    ```

### Administration

* **Accéder au panel admin :** [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

* **Compte par défaut (pour évaluation)** :
    Pour faciliter l'évaluation, un compte administrateur est pré-configuré avec la base de données initiale.

  * **Utilisateur :** `admin`
  * **Mot de passe :** `Abc1234!`

* **Créer un nouvel administrateur** :
    Pour le développement, il est recommandé de créer votre propre compte.

    ```bash
    python manage.py createsuperuser
    ```

---

## Déploiement Automatisé (CI/CD)

### Vue d'ensemble du Pipeline

Le déploiement est entièrement automatisé via GitHub Actions. Tout `push` sur la branche `master` déclenche le workflow suivant :

1. **Build & Test :** Installe les dépendances, exécute `flake8` et `pytest`.
2. **Containerize :** Si les tests passent, une image Docker est construite et poussée sur Docker Hub.
3. **Deploy :** Si l'image est publiée, un "deploy hook" est appelé pour mettre à jour l'application sur Render.

### Configuration pour un Fork

Pour faire fonctionner le pipeline sur votre propre fork, configurez les secrets suivants dans les 
`Settings > Secrets and variables > Actions` de votre dépôt GitHub :

* `DOCKERHUB_USERNAME` : Votre nom d'utilisateur Docker Hub.
* `DOCKERHUB_TOKEN` : Un token d'accès Docker Hub.
* `RENDER_DEPLOY_HOOK_URL` : L'URL du "deploy hook" de votre service Render.

Configurez également les variables d'environnement (`SECRET_KEY`, `SENTRY_DSN`, `DEBUG=False`) 
directement sur votre service Render pour la production.
