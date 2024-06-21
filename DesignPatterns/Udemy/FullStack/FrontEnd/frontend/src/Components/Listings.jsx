import React, {useState} from 'react'

// React Leaflet
import { MapContainer, TileLayer, Marker, Popup,  } from 'react-leaflet'
import { Icon } from 'leaflet';
// MUI
import Grid from "@mui/material/Grid";
import { AppBar, Typography, Button, Card, CardHeader, CardMedia, CardContent } from '@mui/material';

import houseIconPng from "./Assets/Mapicons/house.png"
import apartmentIconPng from "./Assets/Mapicons/apartment.png"
import officeIconPng from "./Assets/Mapicons/office.png"

// Assets
import img1 from "./Assets/image1.jpg"
import myListings from './Assets/Data/Dummydata';
import {makeStyles} from "@mui/styles";

const useStyles = makeStyles({
    cardStyle: {
        margin:"0.5rem",
        border:'1px solid black',
        position:"relative"
    },

    pictureStyle: {
        paddingRight: "1rem",
        paddingLeft:"1rem",
        height:"20rem",
        width:"30rem"
    },

    priceOveraly: {
        position: "absolute",
        backgroundColor:"green",
        zIndex:"1000",
        color:"white",
        top:"100px",
        left:"20px",
        padding:"5px",
    }
})

const Listings = () => {
    const classes = useStyles();
    const houseIcon = new Icon({
        iconUrl: houseIconPng,
        iconSize: [40,40],
    });

    const apartmentIcon = new Icon({
        iconUrl: apartmentIconPng,
        iconSize: [40,40],
    });

    const officeIcon = new Icon({
        iconUrl: officeIconPng,
        iconSize: [40,40],
    });

    const [latitude, setLatitude] = useState(51.505);
    const [longitude, setLongitude] = useState(-0.09);

    function GoEast() {
        setLatitude(51.497)
        setLongitude(0.09)
    }

    function GoCenter() {
        setLatitude(51.505)
        setLongitude(-0.09)
    }


  return (
    <Grid container>
        <Grid item xs={4}>
            {myListings.map((listing) => {
                return (
                <Card key={listing.id} className={classes.cardStyle}>
                    <CardHeader
                    title={listing.title}/>
                <CardMedia
                    className={classes.pictureStyle}
                    component="img"
                    height="194"
                    image={listing.picture1}
                    alt={listing.title}
                />
                <CardContent>
                    <Typography variant="body2" color="text.secondary">
                        {listing.description.substring(0, 200)}...
                    </Typography>
                </CardContent>
                <Typography className={classes.priceOverlay}>${listing.price}</Typography>
                </Card>
                )
            })}
            
        </Grid>
        <Grid item xs={8} style={{marginTop:'0.5rem'}}>
            <AppBar position="sticky">
            <div style={{height: '100vh'}}>
                <MapContainer center={[51.505, -0.09]} zoom={13} scrollWheelZoom={false}>
                    <TileLayer
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    />
                    {myListings.map((listing) => {
                        function IconDisplay() {
                            if(listing.listing_type === 'House') {
                                return houseIcon;
                            }else if(listing.listing_type === "Apartment"){
                                return apartmentIcon;
                            }else if(listing.listing_type === "Office"){
                                return officeIcon;
                            }
                        }
                        return (
                            <Marker 
                                key={listing.id} 
                                icon={IconDisplay()}
                                position={[
                                    listing.location.coordinates[0],
                                    listing.location.coordinates[1]
                                ]}
                            >
                                <Popup>
                                    <Typography variant="h5">{listing.title}</Typography>
                                    <img
                                        src={listing.picture1}
                                        style={{height:'14rem', width:'18rem'}}
                                    />
                                    <Typography variant="body">
                                        {listing.description.substring(0,150)}...
                                    </Typography>
                                    <Button variant="contained" fullwidth>
                                        A Link
                                    </Button>
                                </Popup>
                            </Marker>
                        )
                    })}
                </MapContainer>
            </div>
            </AppBar>
        </Grid>
    </Grid>
    
  )
}

export default Listings