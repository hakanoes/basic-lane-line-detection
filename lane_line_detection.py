import cv2
import numpy as np

cap = cv2.VideoCapture("vi.mp4")
kernel = np.ones((5,5),np.uint8)

while cap.isOpened():
    ret, frame = cap.read()
    resize = frame[300:800,300:1500]
    blur = cv2.GaussianBlur(resize, (5,5), 0)
    hls = cv2.cvtColor(blur, cv2.COLOR_BGR2HLS)
    ret, th = cv2.threshold(hls, 127, 255, cv2.THRESH_BINARY)
        
    lower = np.array([0,102,51])
    upper = np.array([255,255,255])

    mask = cv2.inRange(th, lower, upper)
    edges = cv2.Canny(mask, 75, 150)
    edges = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 0, maxLineGap=100)
    
    if lines is not None:

        for line in lines:
            x, y, w, h = line[0]
            cv2.line(blur, (x,y),(w,h), (0,255,0), 1)
            
    
    cv2.imshow("hls",hls)
    cv2.imshow("th",mask)
    cv2.imshow("test",blur)
    key = cv2.waitKey(30)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows

