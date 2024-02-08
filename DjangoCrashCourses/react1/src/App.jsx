import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { useEffect } from 'react'
import Posts from './components/Posts'
import Header from './components/Header'
import Footer from './components/Footer'

function App() {
  
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const apiURL = 'http://127.0.0.1:8000/api/'
    fetch(apiURL)
      .then((response) => response.json())
      .then((data) => setPosts(data))
  },[]);


  return (
    <>
      <Header/>
      <Posts posts={posts}/>
      <Footer/>
    </>
  )
}

export default App
