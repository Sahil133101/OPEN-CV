import cv2

# Read the image from disk
img = cv2.imread("E:\\OPEN-CV\\Basic\\wallpaper.jpg", cv2.IMREAD_COLOR)

# Display the image in a window
cv2.imshow("My Image", img)

# Wait for a key press indefinitely
cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()
