// Local Project
// Your Code
// Core Node Packages
// Dependencies (3ed party) ---> express
//                          ---> body-parse
// 

const fs = require('fs')

const requestHandler = (req,res) => {
    const url = req.url;
    const method = req.method;
    if(url === '/'){
        res.write('<html>');
        res.write('<head><title>My first pagef</title></head>');
        res.write('<body><form action="/message" method="POST"><input type="text" name="message"><button type="submit">Send</button></form></body>');
        res.write('</html>');
        return res.end();
    }
    if(url === '/message' && method === 'POST') {
        // on allows us listen on events , data events, functions which will be executed for every incoming 
        // data piece
        const body = [];
        req.on('data', (chunk) => {
            console.log(chunk);
            body.push(chunk);
        });
    
        req.on('end', () => {
            const parsedBody = Buffer.concat(body).toString();
            const message = parsedBody.split('=')[1];
            fs.writeFile('message.txt',message, (error) => {
                res.statusCode = 302;
                res.setHeader('Location','/')
                return res.end();
            });
        });
    }
    res.setHeader('Content-Type', 'text/html')
    res.write('<html>');
    res.write('<head><title>My first page</title></head>');
    res.write('<body><h1>Hello from my node js server</h1></body>');
    res.write('</html>');
    res.end();
}


// module.exports = {
//     handler:requestHandler,
//     someText:'Some hard coded text'
// };

module.exports.handler = requestHandler;
module.exports.someText = 'Some hard coded text';