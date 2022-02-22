import cv2


cam = cv2.VideoCapture(0)

while True:
    ret_val, image = cam.read()



    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
    # show it
    

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # draw all contours
    image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    cv2.imshow("Multiple Color Detection in Real-TIme", image)
    cv2.imshow("ajao bhai" , gray)

    # show the image with the drawn contours
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cam.release()
        cv2.destroyAllWindows()
        break