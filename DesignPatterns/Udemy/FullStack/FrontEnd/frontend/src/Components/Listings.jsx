import React from 'react'

// React Leaflet
import { MapContainer, TileLayer, Marker, Popup,  } from 'react-leaflet'
import { Icon } from 'leaflet';
// MUI
import Grid from "@mui/material/Grid";
import { AppBar, Typography, Button } from '@mui/material';

import houseIconPng from "./Assets/Mapicons/house.png"
import apartmentIconPng from "./Assets/Mapicons/apartment.png"
import officeIconPng from "./Assets/Mapicons/office.png"

// Assets
import img1 from "./Assets/image1.jpg"

const Listings = () => {
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

  return (
    <Grid container>
        <Grid item xs={4}>
            <Typography variant="h1">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus necessitatibus voluptates nam debitis ut.
                 Et aliquam nihil reiciendis nemo dolorem iusto magni, dolor ullam itaque accusamus totam veritatis fugit illum
                  deleniti quaerat eligendi odio architecto cum culpa perspiciatis soluta ipsa delectus? Repellat rerum in omnis 
                  sed nemo quam reprehenderit labore eius molestiae consectetur facere at fugiat qui vel esse recusandae praesentium, 
                  quo pariatur sunt tempora aspernatur culpa. Beatae dolores, deleniti quam quia, laboriosam vel unde corrupti vero quos dolorem,
                   maiores molestias impedit tempore cum 
                alias dolore soluta minus! Accusamus blanditiis illum corrupti neque libero corporis et magnam id impedit ex.
            </Typography>
        </Grid>
        <Grid item xs={8}>
            <AppBar position="sticky">
            <div style={{height: '100vh'}}>
                <MapContainer center={[51.505, -0.09]} zoom={13} scrollWheelZoom={false}>
                    <TileLayer
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    />
                    <Marker icon={houseIcon} position={[51.505, -0.09]}>
                        <Popup>
                            <Typography variant="h5">A title</Typography>
                            <img src={img1} style={{height:'14rem', width:'18rem'}}/>
                            <Typography variant="body1">This is some text below the title</Typography>
                            <Button variant="contained">A Link</Button>
                        </Popup>
                    </Marker>
                </MapContainer>
            </div>
            </AppBar>
        </Grid>
    </Grid>
    
  )
}

export default Listings