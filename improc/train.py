from ultralytics import YOLO
import os

# Load a model
# Load a model
model = YOLO('model/yolov8n.yaml')  # build a new model from YAML

# Train the model
results = model.train(data= os.getcwd() + '/datasets/cones/data.yaml', epochs=2, imgsz=255)