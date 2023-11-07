from ultralytics import YOLO
import os

# Load a model
# Load a model
model = YOLO('model/best.pt')  # build a new model from YAML

# Train the model
results = model.train(data= os.getcwd() + '/datasets/amz_yolov8/data.yaml', epochs=100, imgsz=255)

success = model.export()