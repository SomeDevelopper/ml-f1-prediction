from flask import Flask, render_template, request
import pandas as pd
import mlflow

model_dir = 'models/'

app = Flask(__name__)

mlflow.set_tracking_uri('http://127.0.0.1:5001')

@app.route('/')
def home():
    return {'Reponse': 'Bien arrivé'}

MODEL_URI = 'runs:/a83478931323472c840fc41e4657db31/LGBMClassifier'
loaded_model = mlflow.pyfunc.load_model(MODEL_URI)

@app.route("/predict", methods=['POST'])
def predict():
    try:
        if 'fichier' not in request.files:
            return {"error": "Aucun fichier trouvé"}
        fichier = request.files['fichier']
        if fichier.filename == '':
            return {"error": "Aucun fichier sélectionné"}
        df = pd.read_csv(fichier)
        if 'Driver' in df.columns:
            df = df.drop(columns=['Driver', 'Stint', 'RaceElapsedTime', 'WindDirection', 'Year', 'PitStopNextLap'])
        prediction = loaded_model.predict(df)
        print(prediction)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        print(e)
        return {"error": str(e)}


if __name__ == '__main__':
    app.run(port=5051, debug=True)