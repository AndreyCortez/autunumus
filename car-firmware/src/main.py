from servidor import *
from can_functions import *
import can
import cv2
import pickle
import struct

################################## CONFIGURAÇÂO CAN ####################################

can_init()

bus = can.interface.Bus(channel='can0', bustype='socketcan')
message = can.Message(arbitration_id=0x0, data=[0, 0, 0, 0], is_extended_id=False)
bus.send(message)

################################### CONFIGURAÇÃO WEBCAM ##################################

#cap = cv2.VideoCapture(0)


################################## CONFIGURAÇÂO DO SERVIDOR ##############################

servidor_init()
servidor_wait_connection()

def processar_mensagem(msg):

    command = msg.split(",")
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

servidor_bind_mensagem(processar_mensagem)

############################ LOOP DE EXECUÇÂO PRINCIPAL DO PROGRAMA ############################

def setar_valores_velocidade():
    pass


while True:
    #ret, frame = cap.read()
    #data = pickle.dumps(frame)
    #message_size = struct.pack("L", len(data))
    # print("enviando mensagem")
    #servidor_enviar_mensagem(message_size + data)
    time.sleep(0.2)




cliente.close()
bus.shutdown()