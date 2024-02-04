import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import DataFetch from './components/DataFetch'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <DataFetch/>
    
    </>
  )
}

export default App
