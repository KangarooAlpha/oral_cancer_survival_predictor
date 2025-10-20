import type { ApiInput, ApiOutput } from "../types/types"

const url:string = import.meta.env.API_URL
export const callApi = async(
    input: ApiInput): Promise<ApiOutput> => {
    const response = await fetch(`${url}/api/product`, {
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