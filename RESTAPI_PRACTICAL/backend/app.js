const express = require('express');
const bodyParser = require('body-parser');
const feedRoutes = require('./routes/feed');

const app = express();

// app.use(bodyParser.urlencoded()); 

app.use(bodyParser.json()); // application/json

app.use((req,res,next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    next();
});

// feed everything on these routes
app.use('/feed', feedRoutes);

app.listen(8080);

// CORS 
// Cross Origin Resource Sharing 

// Client 
// localhost:3000
// Server
// localhost:3000

// if client and server run on different ports we have error cors error