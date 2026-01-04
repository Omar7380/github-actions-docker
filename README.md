# 🚀 CI/CD avec GitHub Actions, Docker et ArgoCD

Ce projet démontre un pipeline CI/CD complet pour une application conteneurisée, utilisant :
- GitHub Actions pour l'automatisation
- Docker pour la conteneurisation
- ArgoCD pour le déploiement sur Kubernetes

## 📋 Structure du projet

```
.
├── .github/workflows/    # Définition des workflows GitHub Actions
│   └── ci-cd.yml        # Pipeline CI/CD complet
├── k8s/                 # Fichiers de configuration Kubernetes
│   ├── deployment.yml   # Configuration du déploiement
│   └── service.yml      # Configuration du service
├── app/                 # Code source de l'application
│   └── app.py           # Application exemple Python
└── Dockerfile           # Fichier de build Docker
```

## 🚀 Configuration requise

1. **Comptes et accès**
   - Compte GitHub
   - Compte Docker Hub
   - Cluster Kubernetes avec ArgoCD installé

2. **Secrets GitHub**
   - `DOCKERHUB_USERNAME`: Votre nom d'utilisateur Docker Hub
   - `DOCKERHUB_TOKEN`: Votre token d'accès Docker Hub
   - `ARGOCD_SERVER`: URL du serveur ArgoCD
   - `ARGOCD_USERNAME`: Nom d'utilisateur ArgoCD
   - `ARGOCD_PASSWORD`: Mot de passe ArgoCD
   - `ARGOCD_AUTH_TOKEN`: Token d'authentification ArgoCD

## 🔧 Comment ça marche

1. **Déclenchement**
   - À chaque push sur la branche `main`
   - Pour chaque pull request vers `main`

2. **Étapes du pipeline**
   - Construction de l'image Docker
   - Publication sur Docker Hub
   - Déploiement automatique via ArgoCD

3. **Versioning**
   - Chaque image est taguée avec le SHA du commit
   - Les tags sont automatiquement gérés

## 🛠 Installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/votre-utilisateur/06-github-actions-docker.git
   cd 06-github-actions-docker
   ```

2. **Configurer les secrets**
   - Allez dans les paramètres de votre dépôt GitHub
   - Accédez à "Secrets and variables" > "Actions"
   - Ajoutez les secrets requis listés ci-dessus

3. **Configurer ArgoCD**
   - Assurez-vous que ArgoCD est installé sur votre cluster
   - Configurez l'application ArgoCD pour pointer vers ce dépôt

## 📚 Documentation

- [GitHub Actions](https://docs.github.com/actions)
- [Docker Documentation](https://docs.docker.com/)
- [ArgoCD Documentation](https://argo-cd.readthedocs.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

