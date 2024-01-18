const express = require('express');
const path = require('path');
const router = express.Router();
const rootDir = require('../util/path')

// /admin/add-product => GET
router.get('/add-product', (req, res, next) => {
    res.sendFile(path.join(rootDir,'views','add-product.html'))
});

// app.get === app.use but only for incoming get requests
// app.post only for incoming post requests with this path
// we can use get or post or delete or patch or put to filter requests based on http methods more specific

// /admin/add-product => POST
router.post('/add-product', (req,res,next) => {
    console.log(req.body);
    res.redirect('/')
});

module.exports = router;