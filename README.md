# Gesture Control Presenter 🎮🖐️

Control your Google Slides presentations using hand gestures through your laptop camera using Computer Vision and AI.

This project uses:

* OpenCV
* MediaPipe
* PyAutoGUI

to detect hand gestures and convert them into presentation controls like:

* Next Slide
* Previous Slide
* Start Presentation
* Exit Presentation

---

# 🚀 Features

✅ Control Google Slides using gestures
✅ Real-time hand tracking using AI
✅ Works directly from laptop webcam
✅ No additional hardware required
✅ Beginner-friendly AI + Computer Vision project

---

# 🧠 Gesture Controls

| Gesture          | Action          |
| ---------------- | --------------- |
| ✋ Open Palm      | Next Slide      |
| 🤟 Three Fingers | Previous Slide  |
| ✌️ Two Fingers   | Start Slideshow |
| ✊ Fist           | Exit Slideshow  |

---

# 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI

---

# 📦 Installation

## Step 1 — Clone Project

```bash
git clone https://github.com/shivam-kotwalia/gesture-control
cd gesture-control
```

---

## Step 2 — Install Dependencies

```bash
pip3 install -r requirements.txt
```

## Step 3 — Download Hand Landmarker Model

```bash
python3 setup_models.py
```

---

# ▶️ Run the App

```bash
python3 main.py
```

---

# 💻 macOS Permission Setup

For keyboard control to work on macOS:

Go to:

System Settings → Privacy & Security

Enable permissions for:

* Accessibility
* Input Monitoring

Allow access for:

* Terminal
  OR
* VS Code
  OR
* PyCharm

Without these permissions, the app cannot control Google Slides.

---

# 🎯 How to Use

1. Open Google Slides in Chrome
2. Start slideshow mode
3. Run the Python application
4. Show gestures in front of webcam
5. Control slides hands-free

---

# 📂 Project Structure

```bash
gesture-control/
│
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
├── setup_models.py
└── models/
    └── hand_landmarker.task
```

---

# 📜 requirements.txt

```txt
mediapipe==0.10.35
opencv-python>=4.8.0
pyautogui>=0.9.54
```

---

# 🧩 How It Works

The application:

1. Captures webcam feed using OpenCV
2. Detects hand landmarks using MediaPipe
3. Identifies finger positions
4. Maps gestures to keyboard shortcuts
5. Uses PyAutoGUI to control Google Slides

---

# 🔮 Future Improvements

* Swipe gesture recognition
* Gesture-based laser pointer
* Volume control
* Zoom gestures
* AI-powered custom gesture training
* Multi-hand support

---

# 🎓 Learning Outcomes

This project helps students understand:

* Computer Vision
* AI-based gesture recognition
* Human Computer Interaction (HCI)
* Real-time webcam processing
* Automation using Python

---

# 📸 Demo Idea

Use this project during:

* AI Workshops
* Hackathons
* College Tech Fests
* Computer Vision Sessions
* Smart Classroom Demonstrations

---

# ⚠️ Notes

* Ensure good lighting conditions
* Keep hand visible to webcam
* Avoid cluttered backgrounds for better detection
* Works best at moderate camera distance

---

# Live MediaPipe 
![MediaPipe Hand Tracking Demo](https://google-ai-edge.github.io/mediapipe-samples-web/#/vision/hand_landmarker)
![Google AI Media Pipe] (https://ai.google.dev/edge/mediapipe/solutions/guide)

---

# 👨‍💻 Built With AI + Computer Vision

A futuristic interaction system powered by hand tracking and real-time gesture recognition.