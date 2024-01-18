const express = require('express');

const app = express();

// app.use((req,res,next) => {
//     console.log("first middleware");
//     next();
// });

// app.use((req,res,next) => {
//     console.log("second middleware");
//     res.send('<p>Assignmemt solved</p>')
// });

app.use('/users', (req,res,next) => {
    console.log('/users middleware');
    res.send('<p>The middleware that handles just /users</p>');
});

app.use('/',(req,res,next) => {
    console.log("/ middleware");
    res.send('<p>The middleware that handles just /</p>');
});


app.listen(3000);