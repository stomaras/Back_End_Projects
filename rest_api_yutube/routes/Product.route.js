const express = require('express');
const router = express.Router();
const createError = require('http-errors');
const mongoose = require('mongoose');

const Product = require('../models/Product.model');
const ProductController = require('../controllers/Product.Controller');
router.get('/', ProductController.getAllProducts);

// Create a new product
router.post('/',ProductController.createProduct);

// Get a product by id
router.get('/:id', ProductController.findProductById)

// Update a product by id
router.patch('/:id', ProductController.updateProduct)

// Delete a product by id
router.delete('/:id', ProductController.deleteProduct)

module.exports = router;