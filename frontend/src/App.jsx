import React from 'react'
import './App.css'
import Navbar from "./components/Navbar"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CreateStack from "./pages/createStack"
import { AppProvider } from './utils/AppContext';

function App() {
  return (
    <AppProvider>
      <div className='App'>
        {/* <Router>
      <Routes>
        
      </Routes>
    </Router> */}
        <Navbar />
        <CreateStack />
      </div>
    </AppProvider>

  )
}
export default App
