import cv2
import numpy as np

white_col = (255, 255, 255)  # bgr
blue_col = (255, 0, 0)
green_col = (0, 255, 0)
red_col = (0, 0, 255)

photo = np.zeros((500, 500, 3), dtype='uint8')

i = 0
k = 0
for _ in range(255):
    photo[:, 0 + i: 255 + i] = (0 + k, 0 + k, 0 + k)
    k += 1
    i += 5

cv2.circle(photo, (250, 250), radius=200, color=white_col, thickness=4)

cv2.ellipse(photo, (250, 270), (40, 40), 0, 0, 180, color=green_col, thickness=6)
cv2.ellipse(photo, (250, 270), (80, 80), 0, 0, 180, color=green_col, thickness=6)

cv2.line(photo, (170, 270), (170, 200), color=blue_col, thickness=6)
cv2.line(photo, (210, 270), (210, 200), color=blue_col, thickness=6)
cv2.line(photo, (290, 270), (290, 200), color=blue_col, thickness=6)
cv2.line(photo, (330, 270), (330, 200), color=blue_col, thickness=6)

cv2.line(photo, (170, 200), (210, 200), color=red_col, thickness=6)
cv2.line(photo, (290, 200), (330, 200), color=red_col, thickness=6)

cv2.imshow('U Letter', photo)
cv2.waitKey(0)
