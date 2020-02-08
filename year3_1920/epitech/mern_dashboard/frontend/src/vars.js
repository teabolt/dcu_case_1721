// gather environment variables
// we use a private .env file as supported by React Create App projects

var server_hostname = process.env.REACT_APP_SERVER_HOST
var server_port = process.env.REACT_APP_SERVER_PORT

module.exports = {
    server_hostname: server_hostname,
    server_port: server_port,
    server_uri:  `http://${server_hostname}:${server_port}`,
};