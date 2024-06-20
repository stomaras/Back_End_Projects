import logo from './logo.svg';
import './App.css';
import SecondComponent from './Components/SecondComponent';
import AppleComponent from './Components/AppleComponent';
import Fruit from "./Components/Fruit";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from './Components/Home';
import Login from './Components/Login';
import Listings from './Components/Listings';
import { StyledEngineProvider } from '@mui/material'
import CssBaseline from '@mui/material/CssBaseline';
import Header from './Components/Header';
const theFruits = [
  {id: 1, name:'Apple',color:'red'},
  {id: 2, name:'Orange', color:'orange'},
  {id: 3, name:'Banana', color:'yellow'},
  {id: 4, name:'Pineapple', color:'green'},
  {id: 5, name:'Grape', color:'purple'},
  {id: 6, name:'Strawberry', color:'red'},
  {id: 7, name:'Mango', color:'yellow'},
  {id: 8, name:'Watermelon', color:'green'},
]

function App() {
  return (
    <StyledEngineProvider injectFirst>
      <BrowserRouter>
      <CssBaseline/>
      <Header/>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path='/listings' element={<Listings/>}/>
      </Routes>
    </BrowserRouter>
    </StyledEngineProvider>

  );
}

export default App;
