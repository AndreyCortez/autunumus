import socket

class P2PClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))

    def send_message(self, message):
        self.client_socket.sendall(message.encode())

    def receive_message(self):
        data = self.client_socket.recv(1024)
        return data.decode()

    def close(self):
        self.client_socket.close()


ip = input("digite o ip")
port = int(input("digite a porta"))

# Exemplo de uso:
client = P2PClient(ip, port)
client.connect()
# client.send_message("Olá, Host B!")
# response = client.receive_message()
# print(f'Resposta de Host B: {response}')
# client.close()
