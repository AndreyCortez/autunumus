import socket
import threading

servidor = 0
cliente = 0
ip = '0.0.0.0'  # Deixe '0.0.0.0' para ouvir em todas as interfaces de rede
porta = 12345

def servidor_init():
    global servidor
    global cliente
    
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((ip, porta))

def servidor_wait_connection():
    global cliente

    servidor.listen(5)
    print(f"Servidor ouvindo em {ip}:{porta}")

    cliente, addr = servidor.accept()
    print(f"Conexão de {addr[0]}:{addr[1]} estabelecida")

def handle_client(func):
    while True:
        data = cliente.recv(1024).decode()
        if data != "":
            data = data.split("\n")
            for i in data:
                try:
                    func(i)
                except:
                    print(f"ta dando errado na funcao {func}")

def servidor_bind_mensagem(func):
    client_handler = threading.Thread(target=handle_client, args=(func,))
    client_handler.start()

def servidor_enviar_mensagem(data):
    cliente.sendall(data)

if __name__ == "main":
    pass