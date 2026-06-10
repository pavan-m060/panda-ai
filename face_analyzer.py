from deepface import DeepFace
import cv2

def analyze_face():

    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()

    cap.release()

    if not ret:
        return None

    cv2.imwrite("face.jpg", frame)

    result = DeepFace.analyze(
        img_path="face.jpg",
        actions=["gender", "age"],
        enforce_detection=False
    )

    return {
        "age": result[0]["age"],
        "gender": result[0]["dominant_gender"]
    }