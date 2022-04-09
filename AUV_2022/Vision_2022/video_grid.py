import cv2

cap = cv2.VideoCapture(0)
n_rows = 2
n_images_per_row = 2

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    height, width, ch = frame.shape

    roi_height = height / n_rows
    roi_width = width / n_images_per_row

    images = []

    for x in range(0, n_rows):
        x=int(x)
        for y in range(0,n_images_per_row):
            x=int(x)
            y=int(y)
            tmp_image=frame[int(x*roi_height):int((x+1)*roi_height), int(y*roi_width):int((y+1)*roi_width)]
            images.append(tmp_image)

    # Display the resulting sub-frame
    for x in range(0, n_rows):
        for y in range(0, n_images_per_row):
            x=int(x)
            y=int(y)
            cv2.imshow(str(int(x*n_images_per_row+y+1)), images[int(x*n_images_per_row+y)])
            cv2.moveWindow(str(int(x*n_images_per_row+y+1)), int(100+(y*roi_width)), int(50+(x*roi_height)))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()