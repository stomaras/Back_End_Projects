// core modules
// http, -> launch a server, send requests 
// https, 
// fs,
// path,
// os, 

// we execute node app.js
// start script
// parse code, register variables and functions
// event loop, loop process manage by nodejs -> keep on running as long as there are event listeners registered
// on event listener we did registered and we never unregistered is that incoming request listener we passed with the gelp of createserver 
// behind the scenes multuthreading in order to access multiple requests simultaneously
// process.exit will unregistered


// will run for every request who reaches our server
// request is chunk in multiple parts 
// example incoming request
// stream ---> request body part 1 ---> request body part 2 ---> request body part 3 ---> request body part 4 ---> fully parsed
// buffer is like a bus stop 

// event driven architecture
// express ia all about middleware 
// request -> middleware(req,res,next) => {...} next() ---> Middleware(req,res,next) => {...} res.send() ---> Response
// next is another function has to allow your request to travel in the next midddleware

const http = require('http');
const path = require('path')
const express = require('express');
const bodyParser = require('body-parser');
const expressHbs = require('express-handlebars');
const app = express();
const errorController = require('./controllers/error');

app.set('view engine', 'ejs');
app.set('views', 'views');

const adminRoutes = require('./routes/admin');
const shopRoutes = require('./routes/shop');

// this register some middleware call next in the end , before will do body parsing request 
// not parse all bodies like files or json but can data from forms
app.use(bodyParser.urlencoded({extended:false}))
app.use(express.static(path.join(__dirname, 'public')));

app.use(shopRoutes);
app.use('/admin', adminRoutes);

// use handle all http methods
app.use(errorController.get404);

app.listen(4000);
