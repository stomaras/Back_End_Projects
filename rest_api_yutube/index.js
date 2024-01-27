const express = require('express');
const mongoose = require('mongoose');
const app = express();

app.use(express.json());
app.use(express.urlencoded({extended:true}))

mongoose.connect('mongodb://localhost:27017/RestAPI_youtube')
.then(() => {
    console.log('mongodb is connected');
})

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

app.use((req,res,next) => {
    const error = new Error('Not found');
    error.status = 404;
    next(error);
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

app.listen(3000, () => {
    console.log("server started on port 3000");
})