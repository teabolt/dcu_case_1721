#include <iostream>
#include "network.hpp"


Network::Network(std::string hostname, unsigned short port) 
: _socket(_io_context, udp::endpoint(udp::v4(), port+1))
  // FIXME: what does the endpoint represent here? Why we need a different port number from the server?
{
    // address type, hostname, service type (which port to bind to)
    // we can either leave service empty and set port manually, or pass the port as a string
    udp::resolver resolver(_io_context);
    udp::resolver::results_type endpoints = resolver.resolve(udp::v4(), hostname, std::to_string(port));
    _remote_endpoint = *endpoints.begin();
}


void Network::write(std::string data) {
    /**
     * Send data to the server.
    **/
    _socket.send_to(boost::asio::buffer(data), _remote_endpoint);
    std::cout << "[NETWORK LOG] Wrote: " << data << "\n";
}


size_t Network::read() {
    /** 
     * Read message from server, placing result in reply buffer.
     * Returns number of bytes read.
    **/
    size_t reply_length = _socket.receive_from(
        boost::asio::buffer(reply, max_length), _remote_endpoint);
    return reply_length;
}


std::string Network::extract_payload(size_t reply_length) {
    /**
     * Extract the message part of the buffer.
    **/
    std::string data(reply);
    return data.substr(0, reply_length);
}


std::string Network::read_payload() {
    /**
     * Shortcut for calling read() and extract_payload() in one step.
     **/
    size_t reply_length = read();
    std::string payload = extract_payload(reply_length);
    std::cout << "[NETWORK LOG] Got: " << payload << " ( " << reply_length << " bytes )\n";
    return payload;
};