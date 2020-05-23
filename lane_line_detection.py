import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4",0)

while True:
    ret, frame = cap.read()
    # resize video
    resize = frame[350:800,300:1500]
    # convert to hls
    blur = cv2.GaussianBlur(resize, (5,5), 0)
    hls = cv2.cvtColor(blur, cv2.COLOR_BGR2HLS)
    ret, th = cv2.threshold(hls, 100, 255, cv2.THRESH_BINARY)

    # white masked
    lower_white = np.array([146,146,146])
    upper_white = np.array([255,255,255])
    white_mask = cv2.inRange(hls, lower_white, upper_white)

    # yellow masked
    lower_yellow = np.array([10, 0, 100])
    upper_yellow = np.array([40, 255, 255])
    yellow_mask = cv2.inRange(hls,  lower_yellow, upper_yellow)

    mask = cv2.bitwise_or(white_mask, yellow_mask)
    masked = cv2.bitwise_and(white_mask, yellow_mask)
    edges = cv2.Canny(masked, 75, 150)
    
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=50)


    if lines is not None:
        for line in lines:
            x, y ,w ,h = line[0]
            cv2.line(blur, (x, y), (w, h), (0,255,0), 3)



    cv2.imshow("mask",masked)
    cv2.imshow("blur",th)


    key = cv2.waitKey(25)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()














