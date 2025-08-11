import cv2 as cv
import time

cap = cv.VideoCapture(0)  # Open default webcam

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Cannot access the webcam")
    exit()

while True:
    ret, frame = cap.read()  # Read a new frame
    if not ret:
        print("Failed to grab frame")
        break

    # Convert to grayscale safely
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Show the grayscale frame
    cv.imshow('Live Grayscale Video', gray)

    # Exit loop when 'q' is pressed
    key = cv.waitKey(1) & 0xFF 
    if key == ord('q'): 
        break
    elif key == ord('s'):
        
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"captured_{timestamp}.jpg"
        cv.imwrite(filename, frame)
        print(f"Saved image as {filename}")


# Release the capture and close all OpenCV windows
cap.release()
cv.destroyAllWindows()
