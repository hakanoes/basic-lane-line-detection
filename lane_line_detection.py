import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()
    resize1 = frame[350:900,300:1400]
    resize = cv2.GaussianBlur(resize1, (5,5), 0)
    hsv = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)
    low_yellow = np.array([18,94,140])
    up_yellow = np.array([48,255,255])
    mask = cv2.inRange(hsv, low_yellow, up_yellow)
    edges = cv2.Canny(mask, 75, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180,30 , maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1 ,y1, x2, y2 = line[0]
            cv2.line(resize, (x1, y1), (x2, y2), (0, 255, 0), 2)



    if not ret:
        cap = cv2.VideoCapture("testvideo.mp4")
        continue


    cv2.imshow("try",mask)
    cv2.imshow("res",resize)

    key = cv2.waitKey(25)
    if key  == 27:
        break

cap.release()
cv2.destroyAllWindows()
