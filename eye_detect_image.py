import cv2

img = cv2.imread('profile.jpg', 1)
eye_cascade = cv2.CascadeClassifier('eye.xml')

assert img is not None, "No file given"
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img)
# ret, thresh = cv2.threshold(imgray, 127, 255, 0)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img, contours, -1, (0, 255, 0, 3), 3)
eyes = eye_cascade.detectMultiScale(imgray, 1.3, 5)
for x, y ,w, h in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# cv2.imshow('image', img)

cv2.imshow('image', img)
cv2.waitKey(0) & 0xFF == ord('q')
cv2.destroyAllWindows()