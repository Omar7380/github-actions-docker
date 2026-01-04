# 🚀 GitHub Actions - Déploiement d'Application Conteneurisée

Ce projet contient des exemples de workflows GitHub Actions pour le déploiement d'applications conteneurisées.

## 📋 Fichiers de Workflow

### 1. `exo_initial.yml`
Workflow de base qui s'exécute sur chaque push et pull request.

### 2. `exo_build.yml`
Exemple de build d'une application avec installation des dépendances et exécution des tests.

### 3. `exo_nodejs.yml`
Configuration spécifique pour une application Node.js avec installation et test.

### 4. `exo_variable.yml`
Démonstration de l'utilisation de variables et de secrets dans un workflow.

### 5. `exo_cron.yml`
Exemple de tâche planifiée qui s'exécute selon une expression cron.

## 🛠 Comment utiliser

1. Copiez le fichier de workflow souhaité dans votre dossier `.github/workflows/`
2. Personnalisez les étapes selon votre application
3. Poussez les changements pour déclencher le workflow

## 🔧 Configuration requise

- Compte GitHub
- Dépôt avec votre code source
- Fichier `Dockerfile` pour la conteneurisation

## 📚 Ressources

- [Documentation GitHub Actions](https://docs.github.com/actions)
- [Workflow syntaxe](https://docs.github.com/actions/reference/workflow-syntax-for-github-actions)
- [Actions du marché](https://github.com/marketplace?type=actions)
