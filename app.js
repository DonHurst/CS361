// Express Package
var express = require('express');

const request = require('request')

// Initializing the express server
var app = express();

// Body parser for json -> javascript objects
var bodyParser = require('body-parser')

// Setting up bodyParser to use JSON and urlencoded
app.use(bodyParser.json())


// loading in ports from external file
var ports = require('./package.json/ports.json')
var keywordPort = ports.keywordPort
var catPort = ports.catPort
var dogPort = ports.dogPort

// Start the server
app.listen(keywordPort, function(){
    console.log('Express started on http://localhost:' + keywordPort + '; Press ctrl-c to terminate.');
});

// Tell express to serve files from public folder
app.use(express.static('public'));


// Get Request route
app.get('/', function(req,res) {   

    sendBody = {}
    sendBody.msg = "this is a message from the keyword Generator";
    sendbody = JSON.stringify(sendBody);

    res.status(200).send(keyword.html)

})

app.post('/', function(req,res) {
    res.send(req.body)
    res.sendStatus(200)
})




// Error Catch
app.get('*', function (req, res) {
    res.status(404);
    res.send("The page you requested doesn't exist");
});