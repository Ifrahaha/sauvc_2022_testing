
import numpy as np

import cv2

cam = cv2.VideoCapture(0)

while True:
    ret_val, img = cam.read()


    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grayscale, 30, 100)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)
    print(lines)
    for line in lines:
        for x1, y1, x2, y2 in line:

            imageframe =cv2.rectangle(img, (x1, y1), (x2, y2), (220, 220, 220), 3)


    cv2.imshow("Multiple Color Detection in Real-TIme", imageframe)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        cam.release()
        cv2.destroyAllWindows()
        break