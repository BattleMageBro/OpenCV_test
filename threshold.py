import cv2

img = cv2.imread('nn.jpg')
img =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO_INV)
  
# the window showing output images
# with the corresponding thresholding 
# techniques applied to the input images
# cv2.imshow('Binary Threshold', thresh1)
# cv2.imshow('Binary Threshold Inverted', thresh2)
# cv2.imshow('Truncated Threshold', thresh3)
# cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)


if cv2.waitKey(0) & 0xff == ord('q'): 
    cv2.destroyAllWindows() 