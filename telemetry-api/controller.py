import pygame
import sys
import socket
import time
import cv2
import pickle
import struct


################################### Comunicação com a toradex ########################

# 192.168.15.119 Casa
# 192.168.15.20
# 192.168.55.218 bruno 
ip_servidor = '192.168.15.119'  
porta_servidor = 12345

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((ip_servidor, porta_servidor))


#################################### Interface Visual #################################

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Círculo com Sliders para Gatilhos")

circle_radius = 20
circle_x = screen_width // 2
circle_y = screen_height // 2

circle_center_x = screen_width // 2
circle_center_y = screen_height // 2
circle_radius_limit = 200

circle_speed = 5

gamepad_connected = False

pygame.joystick.init()
num_joysticks = pygame.joystick.get_count()

if num_joysticks > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    gamepad_connected = True

def clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))

debug_text = ""

#################### CV2 PRA VER AS IMAGENS RECEBIDAS #################


cv2.namedWindow('Imagem do Servidor', cv2.WINDOW_NORMAL)


############## LOOP DE EXECUÇÂO #################

running = True

x_axis = 0.0
y_axis = 0.0
left_trigger = 0.0
right_trigger = 0.0


while running:

    ########################### PARTE DE PEGAR INPUT DO CONTROLE E INTERFACE DE DEBUG ####################

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if gamepad_connected:
        left_trigger = (joystick.get_axis(2) + 1) / 2
        right_trigger = (joystick.get_axis(5) + 1) / 2
        axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
        x_axis, y_axis = axes[0], axes[1]
        
        x_axis = clamp(-1, x_axis, 1)
        y_axis = clamp(-1, y_axis, 1)

        debug_text += f"x_axis: {x_axis}, y_axis: {y_axis} \n"

        circle_x = int(circle_center_x + x_axis * circle_radius_limit)
        circle_y = int(circle_center_y + y_axis * circle_radius_limit)

    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (circle_center_x, circle_center_y), circle_radius_limit, 1)
    slider_height = circle_radius_limit * 2

    def draw_slider(screen, color, x, y, height, value):
        pygame.draw.rect(screen, color, (x, y, 20, height))
        pygame.draw.rect(screen, WHITE, (x, y, 20, height), 2)
        slider_pos_y = y + int(height - (value * height))
        pygame.draw.circle(screen, RED, (x + 10, slider_pos_y), 8)

    draw_slider(screen, WHITE, circle_center_x + circle_radius_limit + 20, circle_center_y - slider_height // 2, slider_height, left_trigger)
    draw_slider(screen, WHITE, circle_center_x + circle_radius_limit + 50, circle_center_y - slider_height // 2, slider_height, right_trigger)
    pygame.draw.circle(screen, WHITE, (circle_x, circle_y), circle_radius)

    debug_font = pygame.font.Font(None, 24)
    rendered_text = [debug_font.render(line, True, WHITE) for line in debug_text.split('\n')]
    
    text_x = 10
    text_y = 10

    for text_surface in rendered_text:
        screen.blit(text_surface, (text_x, text_y))
        text_y += text_surface.get_height()

    debug_text = ""

    pygame.display.flip()

    ######################### PARTE DE COMUNICAÇÂO COM O SERVIDOR ##############################

    mensagem = f"{x_axis},{y_axis},{left_trigger},{right_trigger}\n"
    print(mensagem)
    cliente.send(mensagem.encode())
    time.sleep(0.02)

    ########################## PARTE DE RECEBER MENSAGENS ######################################

    # print("recebendo mensagem")
    # data = b''
    # while len(data) < struct.calcsize("L"):
    #     data += cliente.recv(4096)

    # packed_msg_size = data[:struct.calcsize("L")]
    # data = data[struct.calcsize("L"):]

    # msg_size = struct.unpack("L", packed_msg_size)[0]

    # # Recebe o quadro serializado
    # while len(data) < msg_size:
    #     data += cliente.recv(4096)

    # frame_data = data[:msg_size]
    # data = data[msg_size:]

    # # Deserializa o quadro
    # frame = pickle.loads(frame_data)

    # # Exibe o quadro
    # cv2.imshow('Imagem do Servidor', frame)
    
    # # Espera por uma tecla 'q' para encerrar a visualização
    # key = cv2.waitKey(1) & 0xFF
    # if key == ord('q'):
    #     break

    

cliente.close()
pygame.quit()
sys.exit()
