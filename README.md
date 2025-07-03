# 🖱️ Hand Gesture Controlled Virtual Mouse

This project allows you to control your mouse cursor using hand gestures captured via webcam. It uses **MediaPipe** for real-time hand tracking, **OpenCV** for camera input, and **PyAutoGUI** for controlling the mouse and scrolling actions.

## ✨ Features

* Control the mouse cursor with your index finger
* Smooth cursor movement with interpolation
* Scroll up/down by pinching your thumb and ring finger and moving vertically
* Real-time hand tracking and gesture dete

## 🛠️ Technologies Used

* [Python](https://www.python.org/)
* [OpenCV](https://opencv.org/)
* [MediaPipe](https://mediapipe.dev/)
* [PyAutoGUI](https://pyautogui.readthedocs.io/)

## 🧠 How It Works

* Uses your webcam feed to detect hand landmarks via MediaPipe.
* Tracks the **index fingertip** to control mouse movement.
* Detects **pinch gestures** (thumb + ring finger) to trigger scrolling:

  * Move hand up → scroll up
  * Move hand down → scroll down
* Smooths cursor motion using linear interpolation to avoid jittery behavior.

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/gesture-mouse-control.git
cd gesture-mouse-control

# Install dependencies
pip install opencv-python mediapipe pyautogui numpy
```

> Make sure you allow screen control permissions if you're on macOS.

## 🚀 Run the App

```bash
python gesture_mouse.py
```

Press **'q'** to quit the application.

## 🧩 Customization Ideas

* Add more gestures for left-click, right-click, or drag
* Use landmarks from other fingers
* Integrate voice or speech feedback
* Enhance gesture stability with better filtering

## 🛡️ Disclaimer

This project is for educational purposes and might not be suitable for professional use due to gesture recognition sensitivity and hardware variation.

## 📄 License

MIT License

