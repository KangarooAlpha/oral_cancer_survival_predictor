import { useState } from "react"
import type { FormTypes } from "../types/types"
import { callApi } from "../services/api"

export default function Form(){
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

    function getResult(e: React.FormEvent){
        e.preventDefault()

        try{
        const result = callApi({
            gender: parseInt(formData['gender']),
            tobacco_use: parseInt(formData['tobaccoUse']),
            family_history: parseInt(formData['familyHistory']),
            cancer_stage: parseInt(formData['cancerStage']),
            diagnosis: parseInt(formData['diagnosis'])
        })
        console.log(result)
        }
        catch (error){
            console.error('Failed to fetch prediction:', error)
        }
    }

    return(
        <form >
            <div>
                <label>Gender</label>
                <select name="gender" onChange={handleData}>
                    <option value="">Select...</option>
                    <option value="0">Male</option>
                    <option value="1">Female</option>
                </select>
            </div>
            <div>
                <label>Tobacco Use</label>
                <select name="tobaccoUse" onChange={handleData}>
                    <option value="">Select...</option>
                    <option value="0">No</option>
                    <option value="1">Yes</option>
                </select>
            </div>
            <div>
                <label>Family History of Cancer</label>
                <select name="familyHistory" id="familyHistory" onChange={handleData}>
                    <option value="">Select...</option>
                    <option value="0">No</option>
                    <option value="1">Yes</option>
                </select>
            </div>
            <div>
                <label>Cancer Stage</label>
                <select name="cancerStage" id="cancerStage" onChange={handleData}>
                    <option value="">Select...</option>
                    <option value="0">0</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                </select>
            </div>
            <div>
                <label>Currently Diagnosed</label>
                <select name="diagnosis" id="diagnosis" onChange={handleData}>
                    <option value="">Select...</option>
                    <option value="0">No</option>
                    <option value="1">Yes</option>
                </select>
            </div>
            <button type="submit"
             onClick={getResult}
             disabled={!buttonStatus}
            >
            Get Prediction!
            </button>
        </form>
    )    
}