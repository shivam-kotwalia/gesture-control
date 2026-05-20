import cv2
import mediapipe as mp
import pyautogui
import time
from mediapipe.tasks.python import vision
import os

# Get the model path
model_path = os.path.join(os.path.dirname(__file__), "models/hand_landmarker.task")

if not os.path.exists(model_path):
    print(f"Error: Model file not found at {model_path}")
    print("Please run: python3 setup_models.py")
    exit(1)

# Create HandLandmarker with the model
base_options = mp.tasks.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.7,
    min_hand_presence_confidence=0.7,
    min_tracking_confidence=0.7
)
hand_landmarker = vision.HandLandmarker.create_from_options(options)

# For drawing
mp_drawing = vision.drawing_utils

cap = cv2.VideoCapture(0)

last_action = ""
last_time = 0
cooldown = 1.5

def fingers_up(hand_landmarks):
    """Detect which fingers are up based on landmarks"""
    tips = [8, 12, 16, 20]   # Fingertip indices
    pips = [6, 10, 14, 18]   # PIP joint indices

    fingers = []

    for tip, pip in zip(tips, pips):
        # If tip is above pip, finger is up
        if hand_landmarks[tip].y < hand_landmarks[pip].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    # Convert BGR to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Create MediaPipe image
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    
    # Detect hand landmarks
    detection_result = hand_landmarker.detect(mp_image)

    gesture = "Waiting..."

    if detection_result.hand_landmarks:

        for hand_landmarks in detection_result.hand_landmarks:
            
            # Draw hand landmarks
            for landmark in hand_landmarks:
                x = int(landmark.x * w)
                y = int(landmark.y * h)
                cv2.circle(frame, (x, y), 2, (0, 255, 0), 1)
            
            # Draw connections between landmarks
            connections = [
                (0, 1), (1, 2), (2, 3), (3, 4),          # Thumb
                (5, 6), (6, 7), (7, 8),                  # Index
                (9, 10), (10, 11), (11, 12),             # Middle
                (13, 14), (14, 15), (15, 16),            # Ring
                (17, 18), (18, 19), (19, 20),            # Pinky
                (0, 5), (5, 9), (9, 13), (13, 17), (0, 17)  # Palm
            ]
            
            for connection in connections:
                start_idx, end_idx = connection
                start = hand_landmarks[start_idx]
                end = hand_landmarks[end_idx]
                x1, y1 = int(start.x * w), int(start.y * h)
                x2, y2 = int(end.x * w), int(end.y * h)
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)

            fingers = fingers_up(hand_landmarks)
            total = fingers.count(1)

            current_time = time.time()

            if current_time - last_time > cooldown:

                # OPEN PALM -> NEXT SLIDE (4 fingers up)
                if total == 4:
                    pyautogui.press("right")
                    gesture = "Next Slide"
                    last_time = current_time

                # THREE FINGERS -> PREVIOUS SLIDE
                elif total == 3:
                    pyautogui.press("left")
                    gesture = "Previous Slide"
                    last_time = current_time

                # TWO FINGERS -> START PRESENTATION
                elif total == 2:
                    pyautogui.hotkey("command", "enter")
                    gesture = "Start Slideshow"
                    last_time = current_time

                # FIST -> EXIT PRESENTATION (0 fingers up)
                elif total == 0:
                    pyautogui.press("esc")
                    gesture = "Exit Slideshow"
                    last_time = current_time

    cv2.putText(
        frame,
        gesture,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Google Slides Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()