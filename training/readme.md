# Oral Cancer Survival Predictor
Predict 5-year survival rate categories for oral cancer patients using multiple machine learning models. 

A detailed report analyzing all models used in this project is available [here](https://docs.google.com/document/d/1Hag81RdMI49xmM5vXTSMjn3jPuXENdJUKNGrTWvNOHc/edit?usp=sharing).
It includes:
- A comparison of model accuracies
- Evaluation metrics and confusion matrices
- Feature selection methods and their results

The dataset used in this analysis can be found on [Kaggle](https://www.kaggle.com/datasets/ankushpanday2/oral-cancer-prediction-dataset/data).
## Features
- Predict survival rate categories using Decision Tree, KNN, SVM, XGBoost, MLP, and Gaussian Naive Bayes models.
- Command-line interface (CLI) for easy predictions.
- Models trained on oral cancer dataset with relevant features.
- Docker container support for easy deployment.
## Requirements
- Python 3.7+
- Required Python packages (see requirements.txt)
## Installation
Clone the repo:
```
git clone https://github.com/KangarooAlpha/oral_cancer_survival_predictor.git
cd oral_cancer_survival_predictor
```
Install dependencies:
```
pip install -r requirements.txt
```
## Usage
### CLI Prediction
Run the prediction script with required feature flags:
```
python3 predict.py --Gender 1 --Tobacco_Use 0 --Family_History_of_Cancer 1 --Cancer_Stage 2 --Oral_Cancer_Diagnosis 1
```
- `--Gender`: 0 (Male), 1 (Female)
- `--Tobacco_Use`: 0 (No), 1 (Yes)
- `--Family_History_of_Cancer`: 0 (No), 1 (Yes)
- `--Cancer_Stage`: 0, 1, 2, 3, 4
- `--Oral_Cancer_Diagnosis`: 0 (No), 1 (Yes)
### Output: Predictions from all models, e.g.:
```
Predicted Survival Rate Category:
- DT: High (60% - 80%)
- KNN: Moderate (40% - 60%)
- SVM: High (60% - 80%)
- XG: High (60% - 80%)
- MLP: High (60% - 80%)
- GNB: Moderate (40% - 60%)
```
## Project Structure
```
oral_cancer_survival_predictor/
├── models/                 # Serialized model files (*.pkl)
├── output/                 # Generated plots and confusion matrices
├── predict.py              # CLI prediction script
├── model_training.py       # Model training and evaluation script
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker setup file
├── oral_cancer_prediction_dataset.csv # Dataset file
└── README.md               # This file
```

## Docker Usage
Build Docker Image
```
docker build -t oral_cancer_predictor .
```
Run Container with Default Prediction
```
docker run --rm oral_cancer_predictor
```
Run Container with Custom Inputs
```
docker run --rm oral_cancer_predictor python3 predict.py --Gender 0 --Tobacco_Use 1 --Family_History_of_Cancer 0 --Cancer_Stage 1 --Oral_Cancer_Diagnosis 1
```
## Notes
Make sure the models/ directory contains trained model files (*.pkl).

Input feature names and types must be exact as specified.

The models expect the features in this order:

> Gender, Tobacco Use, Family History of Cancer, Cancer Stage, Oral Cancer (Diagnosis)
## License
MIT License

