
import Form from './components/form'
import './App.css'
import { useState } from 'react'
import type { ApiOutput } from './types/types'
import Result from './components/result'

function App() {
  const [result, setResult] = useState<ApiOutput>()
  const [loading, setLoading] = useState<Boolean>(false)
  const [error, setError] = useState<String|undefined>()

  return (
    <div className='min-h-screen bg-gradient-to-br from-blue-50 to-indigo-200 py-12 px-4'>
      <div className='max-w-6xl mx-auto'>
        <header className='text-center mb-12'>
          <h1 className='text-4xl font-bold text-gray-900 mb-2'>
            Oral Survival Cancer Predictor
          </h1>
          <p className='text-gray-600'>
            Multi-model machine learning predictions for 5-year survival rates of oral cancer patients
          </p>
        </header>

        <Form 
        setResult={setResult} 
        loading={loading} 
        setLoading={setLoading}
        setError={setError}/>

        {error && (
          <div className='max-w-2xl mx-auto mt-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded'>
            {error}
          </div>
        )}

        {result && <Result result={result}/>}

        <footer className='mt-12 text-center text-gray-600 text-sm'>
          <p>Built with React, Typescript and Python</p>
          <p className='mt-2'>
            Models: Decision Tree, KNN, SVM, XGBoost, MLP, Gaussian Naive Bayes
          </p>
        </footer>

      </div>
    </div>
  )
}

export default App
