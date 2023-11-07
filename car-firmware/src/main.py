from network_comunication.server_socket import P2PServer
import socket

# Endereço IP e porta em que o servidor vai ouvir as conexões
ip = '0.0.0.0'  # Deixe '0.0.0.0' para ouvir em todas as interfaces de rede
porta = 12345

# Cria um soquete do tipo servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liga o soquete ao endereço e porta especificados
servidor.bind((ip, porta))

# Começa a ouvir por conexões
servidor.listen(5)
print(f"Servidor ouvindo em {ip}:{porta}")

# Aceita uma conexão
cliente, addr = servidor.accept()
print(f"Conexão de {addr[0]}:{addr[1]} estabelecida")

while True:
    mensagem = input("Digite a mensagem: ")
    cliente.send(mensagem.encode())
    if mensagem == "encerrar":
        break

# Fecha a conexão do cliente
cliente.close()
