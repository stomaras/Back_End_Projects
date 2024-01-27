const express = require('express');
const router = express.Router();
const Product = require('../models/Product.model');

router.get('/', async (req, res, next) => {
    try {
        const results = await Product.find({},{__v:0});
        // const results = await Product.find({}, {name:1, 
        //     price:1,
        //     _id:0
        // });
        // const results = await Product.find({price: 345}, {});
        res.send(results);
    }catch(error){

    }
});

// Create a new product
router.post('/', async (req, res, next) => {
    try {
        const product = new Product(req.body);
        const result = await product.save();
        res.send(result);
    }catch(err){
        console.log(err.message);
    }
});

// Get a product by id
router.get('/:id', async (req,res,next) => {
    const id = req.params.id;
    try {
        const product = await Product.findById(id);
        res.send(product)
    }catch(error){
        console.log(error.message);
    }
})

// Update a product by id
router.patch('/:id', async(req,res,next) => {
    try {
        const id = req.params.id
        const updates = req.body
        const options = {new: true};

        const result = await Product.findByIdAndUpdate(id,updates,options)
        res.send(result);
    }catch(error){
        console.log(error.message);
    }
})

// Delete a product by id
router.delete('/:id', async(req,res,next) => {
    const id = req.params.id;
    try {
        const result = await Product.findByIdAndDelete(id);
        res.send(result);
    }catch(error){
        console.log(error.message);
    }
})

module.exports = router;