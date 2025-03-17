#!/bin/bash

# Configuration des paramètres
MLFLOW_PORT=5001
MLFLOW_HOST="0.0.0.0"
BACKEND_URI="sqlite:///mlflow.db"  # Utiliser PostgreSQL/MySQL si nécessaire
ARTIFACT_PATH="./mlruns"

echo "🚀 Démarrage du serveur MLflow sur http://${MLFLOW_HOST}:${MLFLOW_PORT}..."

# Activer l'environnement virtuel si nécessaire
# source venv/bin/activate  # Décommentez si vous utilisez un venv

# Lancer MLflow
mlflow server \
    --host $MLFLOW_HOST \
    --port $MLFLOW_PORT \
    --backend-store-uri $BACKEND_URI \
    --default-artifact-root $ARTIFACT_PATH