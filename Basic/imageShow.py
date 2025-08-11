import cv2 as cv
path = r"E:\OPEN-CV\Basic\wallpaper.jpg"
img = cv.imread(path, -1)
resized = cv.resize(img, (800, 600)) 
cv.imshow("image", resized)  # Don't overwrite img!
cv.waitKey(5000)
cv.destroyAllWindows()

cv.imwrite('xyz.jpg',resized)
