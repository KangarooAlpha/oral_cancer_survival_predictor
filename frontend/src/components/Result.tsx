import type { ApiOutput } from "../types/types";
import Card from "./Card";

interface Props{
    result: ApiOutput
}

export default function Result({result}:Props){
    const modelNames = {
        dt: 'Decision Tree',
        knn: 'K-Nearest Neighbors',
        svm: 'Support Vector Machine',
        xgb: 'XGBoost',
        mlp: 'Neural Network (MLP)',
        gnb: 'Gaussian Naive Bayes'
    }

    return(
        <>
        <div className="max-w-4xl mx-auto mt-8 p-6">
            <h3 className="text-2xl font-bold mb-6 text-center text-gray-800">
                Results: 
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {Object.entries(result.predictions).map(([key,prediction])=>(
                    <Card 
                    key={key}
                    modelName={modelNames[key as keyof typeof modelNames]}
                    prediction={prediction}
                    />
                ))}
            </div>
        </div>
        </>
    )
}