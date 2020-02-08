#include "server.hpp"
#include <iostream>


std::string server_hostname = "127.0.0.1";
unsigned short server_port = 6666;


int main(int argc, char* argv[]) {
    std::cout << "I'm the server\n";
    try {
      Server server(server_hostname, server_port);
      std::cout << "Listening on port " << server_hostname << " host " << server_port << "\n";
    } catch (std::exception& e) {
      std::cerr << e.what() << std::endl;
    }
    return 0;
}