import cv2

img = cv2.imread('profile.jpg', 1)
print([event for event in dir(cv2) if 'EVENT' in event])
assert img is not None, "No file given"

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        print(f'coordinates: {x}, {y}/ rgb: {r}, {g}, {b}')
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"{b}/{g}/{r}"
        cv2.putText(img, text, (x, y), font, 0.5 , (255, 0, 0), 1)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        text = f"{x}, {y}"
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, text, (x, y), font, 0.5, (255, 0, 0), 2)
        cv2.imshow('image', img)


cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)
cv2.waitKey(0) & 0xFF == ord('q')
cv2.destroyAllWindows()