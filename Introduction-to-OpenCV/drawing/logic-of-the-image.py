import cv2
import numpy as np

img = np.zeros((10,10,3), np.uint8)
img[0,0] = 255, 0, 0
img[0,1] = 0, 255, 0
img[0,2] = 0, 0, 255
img[0,3] = 255, 255, 0
img[0,4] = 255, 0, 255
img[0,5] = 0, 255, 255
img[0,6] = 255, 255, 255
img[0,7] = 0, 0, 0
img[0,8] = 127, 127, 127
img[0,9] = 127, 0, 0

img = cv2.resize(img, (512,512), interpolation=cv2.INTER_AREA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()