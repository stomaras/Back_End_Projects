const express = require('express');
const mongoose = require('mongoose');
const createError = require('http-errors');
const dotenv = require('dotenv').config();

const app = express();

app.use(express.json());
app.use(express.urlencoded({extended:true}))

mongoose.connect(process.env.MONGODB_URI)
.then(() => {
    console.log('mongodb is connected');
})

mongoose.connection.on('connected', () => {
    console.log('Mongoose connected to db...');
});

mongoose.connection.on('error', (err) => {
    console.log(err.message);
});

mongoose.connection.on('disconnected', () => {
    console.log('Mongoose connection is disconnected');
});

process.on('SIGINT', () => {
    mongoose.connection.close(() => {
        console.log("Mongoose connection is disconnected due to app termination...");
        process.exit(0);
    });
});

app.all('/test', (req,res) => {
    // console.log(req.query);
    // res.send(req.query);
    // console.log(req.params);
    // res.send(req.params);
    console.log(req.body);
    res.send(req.body);
})

const ProductRoute = require('./routes/Product.route');
app.use('/products', ProductRoute);

// 404 handlers and pass to error handler
app.use((req,res,next) => {
    // const error = new Error('Not found');
    // error.status = 404;
    // next(error);
    next(createError(404,'Not Found'));
})

// Error handler
app.use((err, req, res, next) => {
    res.status(err.status || 500)
    res.send({
        error: {
            status: err.status || 500,
            message: err.message
        }
    })
})


const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log('server started on port ' + PORT + '...');
})