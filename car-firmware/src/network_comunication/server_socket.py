import socket
import threading

class P2PServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = None

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f'Aguardando conexão em {self.host}:{self.port}...')

        threading.Thread(target=self.accept_connection).start()

    def accept_connection(self):
        self.client_socket, self.addr = self.server_socket.accept()
        print(f'Conexão estabelecida com {self.client_socket}:{self.addr}')

    def receive_message(self):
        data = self.client_socket.recv(1024)
        return data.decode()

    def send_message(self, message):
        self.client_socket.sendall(message.encode())

    def close(self):
        self.client_socket.close()
        self.server_socket.close()

# Exemplo de uso:
# server = P2PServer('localhost', 12345)
# server.start()
# # O servidor agora está ouvindo em segundo plano
# # O restante do código pode continuar executando
# message = server.receive_message()
# print(f'Mensagem de Host A: {message}')
# server.send_message("Olá, Host A!")
# server.close()
