import type { ApiInput, ApiOutput } from "../types/types"

const url = "http://0.0.0.0:8000/api/predict"
export const callApi = async(
    input: ApiInput): Promise<ApiOutput> => {
    const response = await fetch(url, {
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