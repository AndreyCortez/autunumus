from PIL import Image
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated
import cv2
import os
from collections import deque

def is_image(filename):
    try:
        with Image.open(filename):
            return True
    except:
        return False

def get_image_files(directory):
    image_files = [os.path.abspath(os.path.join(directory, file)) for file in os.listdir(directory) if is_image(os.path.join(directory, file))]
    return image_files

def circular_image_list(directory):
    image_files = get_image_files(directory)

    if not image_files:
        print("Nenhuma imagem encontrada no diretório.")
        return None

    circular_list = deque(image_files)
    return circular_list

# Exemplo de uso
diretorio = "datasets/amz_dataset/amz/img/"
lista_circular = circular_image_list(diretorio)

# Load a model
model = YOLO('model/best.pt')  # pretrained YOLOv8n model


loop = True
ind = 0

while loop:
    # Run batched inference on a list of images
    results = model(lista_circular[ind])  # return a list of Results objects

    # Process results list
    for result in results:
        boxes = result.boxes  # Boxes object for bbox outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs


    CONE_HEIGHT_CONSTANT = 75.0 * 421.8  # Substitua este valor pelo desejado
    distances = []

    for r in results:
            
            im_array = r.plot() 
            annotator = Annotator(im_array)
            
            boxes = r.boxes
            for box in boxes:
                
                b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
                distance = CONE_HEIGHT_CONSTANT / abs(b[1] - b[3])
                annotator.box_label(b, str(int(distance.item())))
        
    img = annotator.result()  
    cv2.namedWindow('Imagem', cv2.WINDOW_NORMAL)

    # Redefina o tamanho da janela
    cv2.resizeWindow('Imagem', 800, 600)  # Substitua 800 e 600 pelos tamanhos desejados

    cv2.imshow('Imagem', img)     

    while 1:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            loop = False
            break

        if cv2.waitKey(1) & 0xFF == ord('d'):
            ind += 1
            break

        if cv2.waitKey(1) & 0xFF == ord('a'):
            ind -= 1
            break



# for cone in result.boxes:
#     #print(cone.boxes)
#     bounding_rect = cone.xywh  # Substitua pela bounding box fornecida pelo algoritmo de ML

# result.probs = distances

# # Show the results
# for r in results:
#     im_array = r.plot()  # plot a BGR numpy array of predictions
#     im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
#     im.show()  # show image
#     #im.save('results.jpg')  # save image