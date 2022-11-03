import numpy as np
import cv2

canvas = np.zeros((512, 512, 3), dtype="uint8") + 255 # 512x512, 3 channels, unsigned 8 bit integer

# Draw a line
cv2.line(canvas, (0, 0), (511, 511), (255, 0, 0), 5) # (0,0) to (511,511), blue, 5px

# Draw a rectangle
cv2.rectangle(canvas, (384, 0), (510, 128), (0, 255, 0), 3) # (384,0) to (510,128), green, 3px

# Draw a circle
cv2.circle(canvas, (447, 63), 63, (0, 0, 255), -1) # (447,63), radius 63, red, -1 means fill

# Draw an ellipse
cv2.ellipse(canvas, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1) # (256,256), (100,50), 0 degree, 0 to 180 degree, blue, -1 means fill

# Draw a polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(canvas, [pts], True, (0, 255, 255)) # True means close the polygon

p1 = (100, 100)
p2 = (200, 200)
p3 = (300, 100)
p4 = (200, 0)

# Draw a triangle
cv2.line(canvas, p1, p2, (0, 0, 0), 5)
cv2.line(canvas, p2, p3, (0, 0, 0), 5)
cv2.line(canvas, p3, p1, (0, 0, 0), 5)

# draw poliylines
cv2.polylines(canvas, [np.array([p1, p2, p3,p4,])], True, (0, 0, 0), 5)

# Add text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canvas, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA) # 'OpenCV', (10,500), font, 4, white, 2px, anti-aliasing


cv2.imshow("Canvas", canvas) # show the canvas
cv2.waitKey(0) # wait for a key press
cv2.destroyAllWindows() # destroy all windows

