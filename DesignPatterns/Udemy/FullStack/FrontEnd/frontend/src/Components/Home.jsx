import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import { Button, Typography, Grid, AppBar, Toolbar } from '@mui/material'
import { makeStyles } from '@mui/styles'
import CustomCard from './CustomCard'
import { ClassNames } from '@emotion/react'
import city from "./Assets/city.jpg";
import Header from './Header'

const useStyles = makeStyles({
    leftNav:{
        marginRight: 'auto'        
    },

    rightNav: {
        marginLeft: 'auto',
        marginRight: '10rem'
    },

    propertyBtn: {
        backgroundColor:"green",
        color:"white",
        width:"15rem",
        fontSize:"1.1rem",
        marginRight:"1rem",
        "&:hover":{
            backgroundColor:"blue",
        },
    },

    loginBtn: {
        backgroundColor:"white",
        color:"black",
        width:"15rem",
        fontSize:"1.1rem",
        marginLeft:"1rem",
        '&:hover': {
            backgroundColor:"green",
        },
    },

    cityImg: {
        width:"100%",
        height:"92vh"
    },

    overlayText: {
        position: "absolute",
        zIndex: "100",
        top:"100px",
        left:"20px",
        textAlign:'center'
    },

    homeText: {
        color:'white',
        fontWeight:"bolder"
    },

    homeBtn: {
        fontSize:'3.5rem',
        borderRadius:"15px",
        backgroundColor:"green",
        marginTop:"2rem",
        boxShadow:"3px 3px 3px white"
    }
})

const Home = () => {
    const classes = useStyles()
    return (
    <>
        <div style={{position:'relative'}}>
            <img src={city} className={classes.cityImg}/>
            <div className={classes.overlayText}>
                <Typography variant="h1" className={classes.homeText}>
                    FIND YOUR <span style={{color:"green"}}>NEXT PROPERTY</span> ON THE LBREP WEBSITE
                </Typography>
                <Button variant="contained" className={classes.homeBtn}>SEE ALL PROPERTIES</Button>
            </div>
        </div>
    </>
    );
}

export default Home