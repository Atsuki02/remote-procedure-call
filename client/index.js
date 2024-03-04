const net = require('net');
const { nrootRequest } = require('./requests');

// set path where the server is waiting for connection
const path = '/tmp/udp_socket_file'

// connect with the socket
const client = net.createConnection({ path }, () => {
    console.log('Connected to server');

    // send request
    const request = JSON.stringify(nrootRequest)
    client.write(request)
});

// when receiving data, log it to the console and end the connection
client.on('data', function(data) {
    console.log('Received: ' + data)
    client.destroy()
})

// when ending the conneciton, log it to the console
client.on('close', function() {
    console.log('Connection closed');
});