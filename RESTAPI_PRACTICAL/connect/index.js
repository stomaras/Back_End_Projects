const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

mongoose.connect('mongodb://localhost:27017/crud');

const UserSchema = mongoose.Schema({
    name:String,
    age:Number
})

const UserModel = mongoose.model('users', UserSchema)


const app = express();
app.use(bodyParser.json()); // application/json

app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'OPTIONS, GET, POST, PUT, PATCH, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    next();
});

app.get('/getUsers', (req, res) => {
    UserModel.find({}).then(function(users){
        console.log(users);
        res.json(users)
    }).catch(function(err) {
        console.log(err);
    })
})

app.listen(3001, () => {
    console.log("server is running ");
})