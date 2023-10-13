from ultralytics import YOLO
import os

# Load a model
# Load a model
model = YOLO('model/yolov8n.pt')  # build a new model from YAML

# Train the model
results = model.train(data= os.getcwd() + '/datasets/fsoco_yolov8/data.yaml', epochs=10, imgsz=255)