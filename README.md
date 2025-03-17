
# Prédiction F1 avec Machine Learning

Ce projet utilise le machine learning pour prédire les résultats des courses de Formule 1 à partir des données historiques des saisons passées.

## Aperçu
L'objectif est de nettoyer, analyser et modéliser les données des saisons F1 pour prédire les résultats des courses. Le projet inclut des étapes de prétraitement des données, d'ingénierie des caractéristiques, et d'entraînement des modèles.

## Fichiers
- `clean_data.ipynb` : Nettoyage et prétraitement des données.
- `data_analyse.ipynb` : Analyse exploratoire des données (EDA).
- `main.py` : Script principal pour exécuter le modèle et les prédictions.
- `requirements.txt` : Dépendances Python nécessaires.
- `resultat_prediction.csv` : Résultats des prédictions.
- `server_model` : Serveur Flask pour exposé le modèle
- `bash.sh` : permet de lancer le serveur MLFlow

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/SomeDevelopper/ml-f1-prediction.git
   cd ml-f1-prediction
   ```

2. Installez les dépendances et création d'un venv :
   ```bash
   python -m venv .venv
   ```
   ```bash
   pip install -r requirements.txt
   ```

2. Lancer le serveur MLFlow :
   ```bash
   ./bash.sh
   ```
2. Lancer le serveur Flask :
   ```bash
   flask --app server_model/app.py run
   ```

3. Exécutez le modèle de prédiction :
   ```bash
   python main.py
   ```

## License
Ce projet est sous licence Apache-2.0 - consultez le fichier [LICENSE](LICENSE) pour plus de détails.

## Remerciements
Ce projet est inspiré par l'analyse des courses F1 et l'application du machine learning dans le domaine sportif.
