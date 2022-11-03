import cv2

# Read the video from specified path
cam = cv2.VideoCapture("kv.mp4")

# webcam
#cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if ret == 0:
        break

    # webcam
    frame = cv2.flip(frame, 1)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()