####################
Déploiement et CI/CD
####################

Ce projet est configuré pour l'Intégration Continue (CI) et le Déploiement Continu (CD) en utilisant GitHub Actions, Docker et Render.

Résumé du fonctionnement
========================

Le pipeline de déploiement est automatisé et suit les étapes suivantes :

1.  **Déclencheur** : Un `push` vers la branche `master` déclenche automatiquement le workflow GitHub Actions.
2.  **Compilation & Tests (CI)** : Le workflow exécute d'abord un job "Build and Test" qui installe les dépendances, lance le linter (`flake8`), et exécute la suite de tests complète (`pytest`). Il vérifie également que la couverture de test est supérieure à 80 %. Ce job doit réussir pour que le pipeline puisse continuer.
3.  **Conteneurisation (CI)** : Si les tests réussissent, un job "Containerize" construit une image Docker de l'application. Cette image est ensuite taguée avec le SHA unique du commit Git et poussée sur Docker Hub.
4.  **Déploiement (CD)** : Si l'image est poussée avec succès, un dernier job "Deploy" est déclenché. Ce job appelle un "Deploy Hook" spécifique fourni par Render, qui ordonne à Render de récupérer la dernière version de la branche `master` et de redéployer le service avec le nouveau code.

Les modifications poussées sur toute autre branche ne déclencheront que le job "Build & Test", garantissant la qualité du code sans le déployer en production.

Configuration Requise
=====================

Pour exécuter ce pipeline de déploiement sur votre propre version du projet (fork), vous devrez configurer les éléments suivants :

**1. Secrets du dépôt sur GitHub**

Naviguez vers les `Settings` > `Secrets and variables` > `Actions` de votre dépôt GitHub et ajoutez les secrets suivants :

* ``DOCKERHUB_USERNAME`` : Votre nom d'utilisateur Docker Hub.
* ``DOCKERHUB_TOKEN`` : Un token d'accès généré depuis votre compte Docker Hub avec les permissions `Read, Write, Delete`.
* ``RENDER_DEPLOY_HOOK_URL`` : L'URL du "Deploy Hook" fournie par votre service web sur Render (disponible dans l'onglet `Settings` du service).

**2. Variables d'environnement sur Render**

Sur le tableau de bord Render, pour votre service web, naviguez vers l'onglet `Environment` et ajoutez les variables suivantes :

* ``DJANGO_SECRET_KEY`` : Une nouvelle clé secrète générée aléatoirement pour l'environnement de production.
* ``SENTRY_DSN`` : La clé DSN de votre projet Sentry.
* ``DEBUG`` : À définir sur `False`.
* ``ALLOWED_HOSTS`` : L'URL de votre application Render (par exemple, `votre-nom-d-app.onrender.com`).

Étapes du Déploiement
=====================

Une fois la configuration initiale terminée, le processus de déploiement est entièrement automatisé.

1.  Assurez-vous que vos modifications sont sur la branche `master`.
2.  Poussez vos commits sur GitHub :

    .. code-block:: bash

        git push origin master