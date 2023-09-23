from network_comunication.server_socket import P2PServer
import socket


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

server = P2PServer(ip_address, 5690)
server.start()