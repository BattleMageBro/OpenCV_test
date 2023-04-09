import cv2

cam = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier('eye.xml')

while cam.isOpened():
    ret, frame = cam.read()
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    eyes = eye_cascade.detectMultiScale(imgray, 1.3, 5)
    for x, y ,w, h in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()