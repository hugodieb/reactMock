import './App.sass'
import './App.css'
import 'font-awesome/css/font-awesome.min.css'
import React from 'react'
import Routes from './Routes'
import Nav from '@components/navbar/Nav'
import Hero from '@components/hero-body/Hero-body'
import Footer from '@components/footer/Footer'

import { BrowserRouter } from 'react-router-dom'


export default props =>
    <BrowserRouter>        
        <div className="app">           
            <Nav/>
            <Hero />
            <Routes/>
            <Footer />         
        </div>
    </BrowserRouter>