import { useState, type SetStateAction } from "react"
import type { ApiOutput, FormTypes } from "../types/types"
import { callApi } from "../services/api"

interface propTypes{
    setResult: React.Dispatch<SetStateAction<ApiOutput|undefined>>
    loading: Boolean
    setLoading: React.Dispatch<SetStateAction<Boolean>>
    setError: React.Dispatch<SetStateAction<String|undefined>>
}

export default function Form({setResult, loading, setLoading, setError}: propTypes){
    const [formData, setFormData] = useState<FormTypes>({
        gender: '',
        tobaccoUse: '',
        familyHistory: '',
        cancerStage: '',
        diagnosis: ''

    })
    const buttonStatus:boolean = !Object.values(formData).includes('')

    function handleData(e: React.ChangeEvent<HTMLSelectElement>){
        setFormData(prevData=> (
        {...prevData,
            [e.target.name] : e.target.value
        }))
    }

    const getResult = async(e: React.FormEvent)=>{
        e.preventDefault()
        setLoading(true)
        try{
            const response = await callApi({
                gender: parseInt(formData['gender']),
                tobacco_use: parseInt(formData['tobaccoUse']),
                family_history: parseInt(formData['familyHistory']),
                cancer_stage: parseInt(formData['cancerStage']),
                diagnosis: parseInt(formData['diagnosis'])
                })
            setResult(response)
        } catch (error){
            console.error('Failed to fetch prediction:', error)
            setError('Failed to get prediction. Please try again.')
        } finally {
        setLoading(false)
        }
    }
    return(
        <form className="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-lg">

            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-70 mb-2">
                    Gender
                </label>
                <select name="gender"
                    onChange={handleData}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                    <option value="">Select...</option>
                    <option value="0">Male</option>
                    <option value="1">Female</option>
                </select>
            </div>
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-70 mb-2">
                    Tobacco Use
                </label>
                <select name="tobaccoUse" 
                onChange={handleData} 
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                    <option value="">Select...</option>
                    <option value="0">No</option>
                    <option value="1">Yes</option>
                </select>
            </div>
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-70 mb-2">
                    Family History of Cancer
                </label>
                <select name="familyHistory" 
                onChange={handleData} 
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                    <option value="">Select...</option>
                    <option value="0">No</option>
                    <option value="1">Yes</option>
                </select>
            </div>
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-70 mb-2">
                    Cancer Stage
                </label>
                <select name="cancerStage" 
                onChange={handleData} 
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                    <option value="">Select...</option>
                    <option value="0">0</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                </select>
            </div>
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-70 mb-2">
                    Currently Diagnosed
                </label>
                <select name="diagnosis" 
                onChange={handleData} 
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                    <option value="">Select...</option>
                    <option value="0">No</option>
                    <option value="1">Yes</option>
                </select>
            </div>
            <button type="submit"
             onClick={getResult}
             disabled={!buttonStatus}
             className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
            >
            {loading ? 'PRedicting...':'Get Prediction!'}
            </button>
        </form>
    )    
}
