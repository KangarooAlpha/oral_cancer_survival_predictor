import argparse
import joblib
import numpy as np
import pandas as pd

FEATURE_NAMES = [
    'Gender',
    'Tobacco Use',
    'Family History of Cancer',
    'Cancer Stage',
    'Oral Cancer (Diagnosis)'
]

MODEL_FILES = {
    'dt': 'models/dt.pkl',
    'knn': 'models/knn.pkl',
    'svm': 'models/svm.pkl',
    'xg': 'models/xgb.pkl',
    'mlp': 'models/mlp.pkl',
    'gnb': 'models/gnb.pkl',
}

LABEL_MAP = {
    0: "Very Low (<20%)",
    1: "Low (20% - 40%)",
    2: "Moderate (40% - 60%)",
    3: "High (60% - 80%)",
    4: "Very High (>80%)"
}

def preprocess_input(args):
    features = [getattr(args, f.replace(" ", "_").replace("(", "").replace(")", "")) for f in FEATURE_NAMES]
    return np.array(features).reshape(1, -1)

def main():
    parser = argparse.ArgumentParser(description='Predict 5-Year Survival Rate using multiple ML models')

    parser.add_argument('--Gender', type=int, choices=[0, 1], required=True)
    parser.add_argument('--Tobacco_Use', type=int, choices=[0, 1], required=True)
    parser.add_argument('--Family_History_of_Cancer', type=int, choices=[0, 1], required=True)
    parser.add_argument('--Cancer_Stage', type=int, choices=[0, 1, 2], required=True)
    parser.add_argument('--Oral_Cancer_Diagnosis', type=int, choices=[0, 1], required=True)

    args = parser.parse_args()

    input_dict = {
        "Gender": args.Gender,
        "Tobacco Use": args.Tobacco_Use,
        "Family History of Cancer": args.Family_History_of_Cancer,
        "Cancer Stage": args.Cancer_Stage,
        "Oral Cancer (Diagnosis)": args.Oral_Cancer_Diagnosis
    }

    input_df = pd.DataFrame([input_dict], columns=FEATURE_NAMES)

    print("\nPredicted Survival Rate Category:")
    for model_key, model_path in MODEL_FILES.items():
        model = joblib.load(model_path)
        if model_key == 'knn':
            scaler = joblib.load('models/scaler.pkl')
            data = scaler.transform(input_df)
        else:
            data = input_df
        pred = model.predict(data)[0]
        
        label = LABEL_MAP[pred] if pred in LABEL_MAP else str(pred)
        print(f"- {model_key.upper()}: {label}")

if __name__ == '__main__':
    main()
