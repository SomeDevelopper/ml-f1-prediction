import pandas as pd
import requests

# URL de votre API
url = 'http://127.0.0.1:5000/predict'  # Notez que j'ai changé le port à 5051 pour correspondre à votre Flask

# Chemin vers votre fichier CSV
csv_path = 'nor-extended-data-preprocessed.csv'

# Préparation du fichier à envoyer
files = {'fichier': open(csv_path, 'rb')}

try:
    # Envoi de la requête avec le fichier
    res = requests.post(url, files=files)
    
    # Traitement de la réponse
    if res.status_code == 200:
        resultats = res.json()
        df = pd.DataFrame(resultats)
        df.to_csv('resultat_prediction.csv')
        print(f"Prédictions reçues : {resultats}")
    else:
        print(f"Erreur: {res.text}")
finally:
    # N'oubliez pas de fermer le fichier
    files['fichier'].close()