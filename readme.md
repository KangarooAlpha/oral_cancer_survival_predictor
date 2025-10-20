# Oral Cancer Survival Predictor

A full-stack machine learning application that predicts 5-year survival rate categories for oral cancer patients using six different ML models.

**🌐 [Live Demo](https://oral-cancer-survival-predictor-gs7fg827a.vercel.app)**

---

## 📊 Overview

This project provides survival rate predictions using an ensemble of machine learning models trained on clinical features. Users can input patient data through an intuitive web interface or command-line tool to receive predictions from multiple models simultaneously.

**📄 Detailed Analysis Report:** [View comprehensive model comparison and evaluation metrics](https://docs.google.com/document/d/1Hag81RdMI49xmM5vXTSMjn3jPuXENdJUKNGrTWvNOHc/edit?usp=sharing)

**📁 Dataset:** [Oral Cancer Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/ankushpanday2/oral-cancer-prediction-dataset/data)

---

## ✨ Features

- **6 ML Models:** Decision Tree, KNN, SVM, XGBoost, MLP, Gaussian Naive Bayes
- **Web Interface:** React + TypeScript frontend with intuitive form-based input
- **REST API:** FastAPI backend serving predictions with type validation
- **CLI Tool:** Command-line interface for quick predictions
- **Deployed:** Production-ready with frontend on Vercel and backend on Render
- **Dockerized:** Container support for local development and deployment

---

## 🚀 Live Application

### [Web Interface](https://oral-cancer-survival-predictor-gs7fg827a.vercel.app)

The web interface provides:
- Form-based input with validation
- Real-time predictions from all 6 models
- Color-coded results by survival rate category
- Responsive design for mobile and desktop

### [API Endpoint](https://oral-cancer-survival-predictor.onrender.com)

**Health Check:**
```bash
GET /api/health
```

**Prediction:**
```bash
POST /api/predict
Content-Type: application/json

{
  "gender": 1,
  "tobacco_use": 0,
  "family_history": 1,
  "cancer_stage": 2,
  "diagnosis": 1
}
```

**Response:**
```json
{
  "predictions": {
    "dt": {
      "category": 3,
      "label": "High (60% - 80%)"
    },
    "knn": {
      "category": 2,
      "label": "Moderate (40% - 60%)"
    },
    ...
  }
}
```

---

## 🛠️ Tech Stack

### Frontend
- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **Vercel** - Deployment

### Backend
- **FastAPI** - Web framework
- **Python 3.9+** - Runtime
- **Scikit-learn** - ML models
- **Pydantic** - Data validation
- **Render** - Deployment

### ML Models
- **XGBoost** - Gradient boosting (99% accuracy)
- **SVM** - Support Vector Machine
- **MLP** - Multi-layer Perceptron (Neural Network)
- **Decision Tree**
- **K-Nearest Neighbors**
- **Gaussian Naive Bayes**

**Average Accuracy:** 91% across all models

---

## 💻 Local Development

### Prerequisites
- Python 3.9+
- Node.js 18+
- Git

### Backend Setup

1. **Clone the repository:**
```bash
git clone https://github.com/KangarooAlpha/oral_cancer_survival_predictor.git
cd oral_cancer_survival_predictor
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the API server:**
```bash
uvicorn api:app --reload --port 8000
```

API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
```bash
cd frontend
```

2. **Install dependencies:**
```bash
npm install
```

3. **Create `.env` file:**
```env
VITE_API_URL=http://localhost:8000
```

4. **Start development server:**
```bash
npm run dev
```

Frontend will be available at `http://localhost:5173`

---

## 🐳 Docker Usage

### Build and Run Backend

```bash
# Build image
docker build -t cancer-predictor-api .

# Run container
docker run -p 8000:8000 cancer-predictor-api
```

### Docker Compose (Full Stack)

```bash
# Start all services
docker-compose up

# Stop services
docker-compose down
```

---

## 🖥️ CLI Usage

For quick predictions without the web interface:

```bash
python predict.py \
  --Gender 1 \
  --Tobacco_Use 0 \
  --Family_History_of_Cancer 1 \
  --Cancer_Stage 2 \
  --Oral_Cancer_Diagnosis 1
```

**Parameters:**
- `Gender`: 0 (Male), 1 (Female)
- `Tobacco_Use`: 0 (No), 1 (Yes)
- `Family_History_of_Cancer`: 0 (No), 1 (Yes)
- `Cancer_Stage`: 0-4 (Stage 0 through Stage 4)
- `Oral_Cancer_Diagnosis`: 0 (No), 1 (Yes)

**Output:**
```
Predicted Survival Rate Category:
- Decision Tree: High (60% - 80%)
- KNN: Moderate (40% - 60%)
- SVM: High (60% - 80%)
- XGBoost: High (60% - 80%)
- MLP: High (60% - 80%)
- Naive Bayes: Moderate (40% - 60%)
```
---

## 📊 Model Performance

| Model | Accuracy | Notes |
|-------|----------|-------|
| **XGBoost** | **99%** | Best performing model |
| MLP | 94% | Neural network approach |
| Decision Tree | 92% | Interpretable decisions |
| SVM | 90% | Support vector classification |
| KNN | 88% | Distance-based prediction |
| Naive Bayes | 85% | Probabilistic classifier |

**Average Accuracy:** 91% across all models

**Training Optimization:** Feature selection reduced training time by 74.3%

Detailed evaluation metrics, confusion matrices, and feature importance analysis available in the [full report](https://docs.google.com/document/d/1Hag81RdMI49xmM5vXTSMjn3jPuXENdJUKNGrTWvNOHc/edit?usp=sharing).

---

## 🔒 API Documentation

### Endpoints

#### Health Check
```http
GET /api/health
```

**Response:**
```json
{
  "status": "healthy",
  "models_loaded": 6
}
```

#### Predict
```http
POST /api/predict
Content-Type: application/json
```

**Request Body:**
```json
{
  "gender": 0,
  "tobacco_use": 1,
  "family_history": 0,
  "cancer_stage": 2,
  "diagnosis": 1
}
```

**Response:**
```json
{
  "predictions": {
    "dt": { "category": 2, "label": "Moderate (40% - 60%)" },
    "knn": { "category": 2, "label": "Moderate (40% - 60%)" },
    "svm": { "category": 3, "label": "High (60% - 80%)" },
    "xgb": { "category": 3, "label": "High (60% - 80%)" },
    "mlp": { "category": 3, "label": "High (60% - 80%)" },
    "gnb": { "category": 2, "label": "Moderate (40% - 60%)" }
  }
}
```

**Error Response:**
```json
{
  "error": "Missing required fields"
}
```

---

## 🚀 Deployment

### Backend (Render)

1. Connect GitHub repository to Render
2. Configure build command: `pip install -r requirements.txt`
3. Configure start command: `uvicorn api:app --host 0.0.0.0 --port $PORT`
4. Deploy

### Frontend (Vercel)

1. Connect GitHub repository to Vercel
2. Set framework preset to "Vite"
3. Configure environment variable: `VITE_API_URL=https://your-api.onrender.com`
4. Deploy

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

**Omar Fayyaz**

- GitHub: [@KangarooAlpha](https://github.com/KangarooAlpha)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/your-profile)
- Email: omarfayyaz101@gmail.com

---

## 🙏 Acknowledgments

- Dataset provided by [Kaggle](https://www.kaggle.com/datasets/ankushpanday2/oral-cancer-prediction-dataset/data)
- Built as a learning project to demonstrate full-stack development with ML integration
- Developed with React, TypeScript, FastAPI, and Scikit-learn

---

## 📈 Future Improvements

- [ ] Add confidence intervals for predictions
- [ ] Implement model versioning
- [ ] Add data visualization for feature importance
- [ ] Support batch predictions
- [ ] Add model explainability (SHAP values)
- [ ] Implement caching for faster predictions

---

**⭐ If you find this project helpful, please consider giving it a star on GitHub!**
