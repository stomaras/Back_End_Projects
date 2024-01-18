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

const express = require('express');

const app = express();
app.use((req, res, next) => {
    console.log('In the middleware');
    next(); // allows the request to continue to the next middleware in line 
});

app.use((req, res, next) => {
    console.log('In the another middleware');
    // ...
});

const routes = require('./routes');

const server = http.createServer(app);

server.listen(3000);


// Summary 
// Client send a request to the server 
// server store to database or manipulate files
// send a response to the client html or json
// client ---> request ---> server ---> response ---> client

// Program Lifecycle and Event Loop
// nodejs uses an event-driven code("Event Loop") for running yout logic
// the createServer() event never finishes by default


// Request and response data is chunk (streams and buffers)
// avoid double responses.

// Node.js and core modules 
// http, https, fs, path, os
// import via require('module')

