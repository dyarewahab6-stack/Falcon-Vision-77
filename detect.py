import cv2
import torch
from ultralytics import YOLO

def run_tactical_detection(source_path="dataset/sample_drone.jpg", conf_threshold=0.5):
    """
    Falcon-Vision-77: Edge AI Object Detection Pipeline
    Designed for real-time target identification using custom YOLOv8 weights.
    """
    print("[INFO] Initializing Falcon-Vision-77 Core Engine...")
    
    # Load model (fallbacks to pre-trained weights if local custom weights unavailable)
    try:
        model = YOLO("weights/best.pt")
        print("[INFO] Custom target detection weights loaded successfully.")
    except Exception as e:
        print("[WARNING] Custom weights not found, using baseline YOLOv8 model.")
        model = YOLO("yolov8n.pt")

    # Run inference on input stream or image source
    results = model.predict(source=source_path, conf=conf_threshold, show=False)
    
    for result in results:
        boxes = result.boxes
        print(f"[RESULTS] Detected {len(boxes)} tactical target(s) in frame.")
        
        for box in boxes:
            cls_id = int(box.cls[0])
            confidence = float(box.conf[0])
            label = model.names[cls_id]
            print(f" -> Target: {label} | Confidence: {confidence:.2f}")

if __name__ == "__main__":
    run_tactical_detection()
  
