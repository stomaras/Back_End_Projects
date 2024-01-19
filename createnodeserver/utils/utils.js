const path = require('path');

const myPath = path.join(
    path.dirname(process.mainModule.filename),
    'data', 
    'products.json'
);

module.exports = myPath;