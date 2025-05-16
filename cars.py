import cv2
import time
import os

# Load the Haar Cascade
cars_cascade = cv2.CascadeClassifier('cars.xml')
if cars_cascade.empty():
    print("Error loading cars.xml. Please check the path.")
    exit()

# Create directory to save screenshots
output_dir = "car_screenshots"
os.makedirs(output_dir, exist_ok=True)

def detect_and_save(frame, frame_id=0):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = cars_cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=4)

    detected = False
    for (x, y, w, h) in cars:
        detected = True
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if detected:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = os.path.join(output_dir, f"car_detected_{timestamp}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Car detected! Screenshot saved to: {filename}")

    return frame

def capture_single_frame():
    cap = cv2.VideoCapture(0)  # 0 = default webcam, or replace with image/video source

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    print("Press 's' to capture frame, or 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        cv2.imshow('Live Frame - Press s to detect car', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            # Detect cars and save screenshot if found
            result_frame = detect_and_save(frame)
            cv2.imshow('Detection Result', result_frame)
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_single_frame()
