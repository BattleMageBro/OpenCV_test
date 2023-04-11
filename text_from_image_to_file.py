import cv2
import pytesseract

img = cv2.imread("images/text.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
dilation = cv2.dilate(thresh, rect_kernel, iterations=1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
im2 = img.copy()

file = open('res.txt', 'w+')
file.write("")
file.close()

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    rect = cv2.rectangle(im2, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cropped = im2[y:y + h, x:x + w]
    file = open('res.txt', 'a')
    text = pytesseract.image_to_string(cropped, lang='rus')
    file.write(text)
    file.write("\n")
    file.close()