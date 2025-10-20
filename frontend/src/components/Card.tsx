import type { Prediction } from "../types/types"


interface Props{
    modelName: string
    prediction: Prediction
}

export default function Card({modelName, prediction}:Props){
    const getColorClass = (category:number) => {
        const colors = [
        'bg-red-100 border-red-500 text-red-800',
        'bg-orange-100 border-orange-500 text-orange-800',
        'bg-yellow-100 border-yellow-500 text-yellow-800',
        'bg-lime-100 border-lime-500 text-lime-800',
        'bg-green-100 border-green-500 text-green-800'
    ]
        return colors[category]
    }
    const color = getColorClass(parseInt(prediction.category))
    return(
        <div className={`p-4 rounded-lg border-l-4 ${color}`}>
            <h4 className="font-bold text-lg mb-2">{modelName}</h4>
            <p className="text-sm font-medium">{prediction.label}</p>
        </div>
    )
}