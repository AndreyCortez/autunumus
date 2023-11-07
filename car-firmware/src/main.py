from network_comunication.server_socket import P2PServer
import socket
import can
import subprocess

################################## CONFIGURAÇÂO CAN ####################################

import os
import time

# Desativa a interface CAN
os.system("ip link set can0 down")
time.sleep(1)

# Configura a interface CAN com baudrate de 500 kbps e ativa o loopback
os.system("ip link set can0 type can bitrate 500000")
time.sleep(1)

# Ativa a interface CAN
os.system("ip link set can0 up")
time.sleep(1)

bus = can.interface.Bus(channel='can0', bustype='socketcan')
message = can.Message(arbitration_id=0x0, data=[0, 0, 0, 0], is_extended_id=False)

#os.system("cansend can0 000#0000")
bus.send(message)

################################## CONFIGURAÇÂO DO SERVIDOR ##############################

ip = '0.0.0.0'  # Deixe '0.0.0.0' para ouvir em todas as interfaces de rede
porta = 12345

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((ip, porta))

servidor.listen(5)
print(f"Servidor ouvindo em {ip}:{porta}")

cliente, addr = servidor.accept()
print(f"Conexão de {addr[0]}:{addr[1]} estabelecida")

############################ LOOP DE EXECUÇÂO PRINCIPAL DO PROGRAMA ############################

while True:
    mensagem = cliente.recv(1024).decode()
    if mensagem != "":
        try:

            #print(f"Cliente diz: {mensagem}")
            command = mensagem.split(",")
            command = [float(i) for i in command]


            turn_direction = command[0]
            turn_intensity = int(abs(command[0]) * 255)
            walk_direction = (-command[2] + command[3])
            walk_intensity = abs(int((-command[2] + command[3]) * 255))

            message = [0,0,0,0,0,0]

            if  turn_direction > 0:
                message[1] = 0
                message[2] = 1
            else:
                message[1] = 1
                message[2] = 0
            
            if  walk_direction > 0:
                message[4] = 1
                message[5] = 0
            else:
                message[4] = 0
                message[5] = 1
            
            message[0] = turn_intensity
            message[3] = walk_intensity

            print(message)

            message = can.Message(arbitration_id=0x2, data=message, is_extended_id=False)
            bus.send(message)
            
            time.sleep(0.02)
        except:
            pass
    if mensagem == "encerrar":
        break



cliente.close()
bus.shutdown()