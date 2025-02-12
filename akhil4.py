import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Get screen size
screen_width, screen_height = pyautogui.size()

# Open camera
cap = cv2.VideoCapture(0)

# Cursor smoothing factors
prev_x, prev_y = pyautogui.position()
alpha = 0.3  # Smoothing factor

# Click Management
last_click_time = 0
click_delay = 0.3  # Delay between clicks to prevent accidental triggers
pinch_active = False
right_click_active = False
drag_active = False  # Drag-and-drop flag

# Distance Calculation Function
def calculate_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

prev_ring_y = 0  # Track previous ring finger Y for scrolling

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally & convert to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame
    result = hands.process(rgb_frame)
    frame_height, frame_width, _ = frame.shape

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get key finger landmarks
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            ring_finger = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]

            # Convert to screen coordinates
            index_x = int(index_finger.x * frame_width)
            index_y = int(index_finger.y * frame_height)

            screen_x = np.interp(index_x, [0, frame_width], [0, screen_width])
            screen_y = np.interp(index_y, [0, frame_height], [0, screen_height])

            # Apply smoothing for better control
            screen_x = prev_x * (1 - alpha) + screen_x * alpha
            screen_y = prev_y * (1 - alpha) + screen_y * alpha
            pyautogui.moveTo(screen_x, screen_y, duration=0.05)  # Faster cursor updates
            prev_x, prev_y = screen_x, screen_y

            # Calculate distances for gestures
            pinch_distance = calculate_distance((ring_finger.x, ring_finger.y), (thumb.x, thumb.y))

            # *Scrolling Detection: Thumb-Ring Finger Pinch*
            if pinch_distance < 0.05:
                ring_y = ring_finger.y

                if prev_ring_y != 0:
                    scroll_delta = prev_ring_y - ring_y
                    if scroll_delta > 0.01:  # Scroll up
                        pyautogui.scroll(60)
                    elif scroll_delta < -0.01:  # Scroll down
                        pyautogui.scroll(-60)

                prev_ring_y = ring_y
            else:
                prev_ring_y = 0  # Reset when pinch gesture is inactive

    # Display the frame
    cv2.imshow("Hand Tracking Mouse", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
