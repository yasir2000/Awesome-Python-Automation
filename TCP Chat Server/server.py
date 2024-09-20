# .env
# This file would contain environment variables.
IP='0.0.0.0'
PORT=3000

import os
import socket
from dotenv import load_dotenv

class Server:
    """Class responsible for managing the socket server."""
    
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """Start the server."""
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(5)
        print(f'Server is listening on {self.ip}:{self.port}')
        
        while True:
            client_socket, address = self.server_socket.accept()
            print(f'Received a connection from {address[0]}:{address[1]}')
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        """Handle communication with a connected client."""
        data = client_socket.recv(4096)
        decoded_data = data.decode()
        print(decoded_data)

        send_message = input('Send message> ')
        client_socket.send(send_message.encode())
        client_socket.close()

if __name__ == '__main__':
    load_dotenv()  # Load environment variables
    ip = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 3000))
    server = Server(ip, port)
    server.start()
