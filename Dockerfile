# Étape de construction
FROM python:3.9-slim as builder

WORKDIR /app

# Copier les fichiers de dépendances
COPY app/requirements.txt .

# Installer les dépendances
RUN pip install --user -r requirements.txt

# Étape d'exécution
FROM python:3.9-slim

WORKDIR /app

# Copier les fichiers de l'application
COPY --from=builder /root/.local /root/.local
COPY app/ .

# Rendre les scripts accessibles
ENV PATH=/root/.local/bin:$PATH
ENV FLASK_APP=app.py

# Exposer le port utilisé par l'application
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
