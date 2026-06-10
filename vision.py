from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect_objects():

    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()

    cap.release()

    if not ret:
        return []

    results = model(frame)

    objects = []

    for box in results[0].boxes:

        cls = int(box.cls[0])

        objects.append(
            results[0].names[cls]
        )

    return list(set(objects))