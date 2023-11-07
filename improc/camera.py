import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator

# Load the YOLOv8 model
model = YOLO('model/best.pt')


# import the opencv library 
import cv2 
  
# define a video capture object 
vid = cv2.VideoCapture(0) 
  
  
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
  
    # Display the resulting frame 
    results = model(frame)

    CONE_HEIGHT_CONSTANT = 75.0 * 421.8  # Substitua este valor pelo desejado
    distances = []


    for r in results:
            
            im_array = r.plot() 
            annotator = Annotator(im_array)
            
            boxes = r.boxes
            for box in boxes:
                
                b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
                distance = CONE_HEIGHT_CONSTANT / (b[2] - b[0])
                annotator.box_label(b, str(distance.item()))
        
    img = annotator.result()  

    # Display the annotated frame
    # Visualize the results on the frame
    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv8 Inference", img)
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 

# Loop through the video frames
# while cap.isOpened():
#     # Read a frame from the video
#     success, frame = cap.read()

#     if success:
#         # Run YOLOv8 inference on the frame