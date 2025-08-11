# Python code to read image
import cv2

# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread("E:\OPEN-CV\Basic\wallpaper.jpg", cv2.IMREAD_COLOR)
cv2.imshow(img)
cv2.waitKey(0)


cv2.destroyAllWindows()
