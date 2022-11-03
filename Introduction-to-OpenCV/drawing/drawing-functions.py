import numpy as np
import cv2

canvas = np.zeros((512, 512, 3), dtype="uint8") + 255 # 512x512, 3 channels, unsigned 8 bit integer

#print(canvas) # 512x512, 3 channels, unsigned 8 bit integer

cv2.imshow("Canvas", canvas) # show the canvas
cv2.waitKey(0) # wait for a key press
cv2.destroyAllWindows() # destroy all windows

