import React from 'react'
import { Link } from 'react-router-dom'

const Home = () => {
  return (
    <div>
        <h1>This is the homepage</h1>
        <br/>
        <Link to="/login">Login</Link>
        <br/>
        <Link to="/listings">Listings</Link>
    </div>
  )
}

export default Home