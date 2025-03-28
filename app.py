from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

# Define input data model
class PatientData(BaseModel):
    age: float
    attention_score: float
    hyperactivity_score: float
    academic_index: float
    bai1_total: float
    sex_female: int
    sex_male: int

app = FastAPI(title="ADHD Detection API")

# Load model and pipeline
pipeline = joblib.load('preprocessing_pipeline.pkl')
model = joblib.load('adhd_model_v1.pkl')

@app.post("/predict")
async def predict(patient: PatientData):
    try:
        # Convert to DataFrame
        input_df = pd.DataFrame([patient.dict()])
        
        # Preprocess and predict
        processed = pipeline.transform(input_df)
        proba = model.predict_proba(processed)[0][1]
        
        return {
            "prediction": int(proba > 0.5),
            "probability": round(proba, 4),
            "interpretation": "High risk" if proba > 0.7 else ("Possible risk" if proba > 0.3 else "Low risk")
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def health_check():
    return {"status": "OK"}