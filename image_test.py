import cv2

img = cv2.imread('images/profile.jpg', 1)

assert img is not None, "No file given"
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img)
print("Height: ", str(img.shape[0]))
print("Weight: ", str(img.shape[1]))
print("Channel count: ", str(img.shape[2]))
b, g, r = img[167,129]
print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))
for i in range(len(img)):
    for j in range(len(img)):
        img[i,j] = (b, g, r)
# cv2.imshow('image', img)

cv2.imshow('image', img)
cv2.waitKey(0) & 0xFF == ord('q')
cv2.destroyAllWindows()