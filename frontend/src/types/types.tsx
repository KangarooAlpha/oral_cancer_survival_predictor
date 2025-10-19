export interface FormTypes{
    gender: string
    tobaccoUse: string
    familyHistory: string
    cancerStage: string
    diagnosis: string
}

export interface ApiInput{
    gender: number
    tobacco_use: number
    family_history: number
    cancer_stage: number
    diagnosis: number
}

interface Prediction{
    category: number
    label: string
}

export interface ApiOutput{
    predictions:{
        dt: Prediction 
        knn: Prediction
        svm: Prediction
        xgb: Prediction
        mlp: Prediction
        gnb: Prediction
    }
}