from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
import joblib
from pydantic import BaseModel
import numpy as np
import uvicorn
from typing import Literal

class Param(BaseModel):
    gender: Literal[1,0]
    tobacco_use: Literal[1,0]
    family_history: Literal[1,0]
    cancer_stage: Literal[1,2,3,4,0]
    diagnosis: Literal[1,0]
    
class Output(BaseModel):
    category: Literal[1,2,3,4,0]
    label: str

app = FastAPI()

models = {
    'dt': joblib.load('models/dt.pkl'),
    'gnb': joblib.load('models/gnb.pkl'),
    'knn': joblib.load('models/knn.pkl'),
    'mlp': joblib.load('models/mlp.pkl'),
    'svm': joblib.load('models/svm.pkl'),
    'xgb': joblib.load('models/xgb.pkl')
}
scalar = joblib.load('models/scaler.pkl')

labels = [
    "Very Low (<20%)",
    "Low (20% - 40%)",
    "Moderate (40% - 60%)",
    "High (60% - 80%)",
    "Very High (>80%)"
]

def resolve_prediction(pred) -> tuple[int | None, str]:
    try:
        index = int(pred)
        if 0 <= index < len(labels):
            return index, labels[index]
    except (ValueError, TypeError):
        pass

    pred_str = str(pred).strip()
    if pred_str in labels:
        return labels.index(pred_str), pred_str

    return None, pred_str

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['GET', 'POST']
)

@app.post('/api/predict')
async def predict(body: Param):
    
    features = np.array([[
        body.gender,
        body.tobacco_use,
        body.family_history,
        body.cancer_stage,
        body.diagnosis
    ]])
    
    scaled_features = scalar.transform(features)
    
    predictions = {}
    for name, model in models.items():
        if name == 'knn':
            input_data = scaled_features
        else:
            input_data = features

        pred = model.predict(input_data)[0]

        category, label = resolve_prediction(pred)
        predictions[name] = {
            'category': category,
            'label': label
        }

    return {'predictions': predictions}
        
           
def get_label(pred):
    labels = {
        0: 'Very Low (<20%)',
        1: 'Low (20% - 40%)',
        2: 'Moderate (40% - 60%)',
        3: 'High (60% - 80%)',
        4: 'Very High (>80%)'
    }
    return(labels[pred])


@app.get('/api/health')
async def health():
    return{'status': 'healthy'}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)