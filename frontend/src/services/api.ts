import type { ApiInput, ApiOutput } from "../types/types"

export const callApi = async(
    input: ApiInput): Promise<ApiOutput> => {
    const response = await fetch(`https://oral-cancer-survival-predictor.onrender.com/api/predict`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(input)
    })
    if (!response.ok){
        throw new Error('Prediction request failed')
    }

    return response.json()
}