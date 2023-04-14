import cv2

cam = cv2.VideoCapture("/dev/video0")
face_cascade = cv2.CascadeClassifier('cascades/frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier('cascades/profilefaces.xml')

while cam.isOpened():
    ret, frame = cam.read()
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(imgray, 1.3, 5)
    profiles = face_cascade.detectMultiScale(imgray, 1.3, 5)
    for x, y ,w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    for x, y ,w, h in profiles:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()