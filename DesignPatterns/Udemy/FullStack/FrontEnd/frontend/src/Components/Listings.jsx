import React, {useState} from 'react'

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
            <Button onClick={GoEast}>GO EAST</Button>
            <Button onClick={GoCenter}>GO CENTER</Button>
        </Grid>
        <Grid item xs={8}>
            <AppBar position="sticky">
            <div style={{height: '100vh'}}>
                <MapContainer center={[51.505, -0.09]} zoom={13} scrollWheelZoom={false}>
                    <TileLayer
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    />
                    <Marker icon={houseIcon} position={[latitude, longitude]}>
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