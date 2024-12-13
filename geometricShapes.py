import numpy as np
import cv2

# img = cv2.imread("assets/image.png", 1) INSTEAD:

# [height, width, channel]
img = np.zeros([480, 640, 3], np.uint8)

# line(img, pt1, pt2, color, thickness)
img = cv2.line(img, (0,0), (255,255), (255,0,0), 5)
img = cv2.arrowedLine(img, (0,255), (255,255), (105,100,0), 5)

# rectangle(img, pt1, pt2, color, thickness, lineType, shift)
# x1,y1 ----
# |         |
# |         |
# --------x2,y2 


# If thickness is -1 it will fill in the rectangle
img = cv2.rectangle(img, (324,0), (510, 128), (0,0,255), 10)

# circle(img, center, radius, color, thickness)
img = cv2.circle(img, (440,60), 30, (0,255,0), -1)

# putText(img, text, starting point, font, font size, color, thickness, linetype)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'lookathim', (10,300), font, 4, (255,255,255), 10, cv2.LINE_AA)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()