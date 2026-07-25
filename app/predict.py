import joblib
import pandas as pd

MODEL_PATH = "../models/random_forest_best.pkl"

model = joblib.load(MODEL_PATH)

def predict(patient_data):

    patient_df = pd.DataFrame([patient_data])

    prediction = model.predict(patient_df[0])

    probability = model.predict_proba(patient_df)[0][1]

    return prediction, probability
