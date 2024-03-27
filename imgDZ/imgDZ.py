import cv2
import numpy as np

colors = {'red': (0, 0, 255),
          'green': (0, 255, 0),
          'purple': (166, 0, 100)
          }

img = cv2.imread('color_text.jpg')
print(img.shape)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.blur(img, (3, 3))

img = cv2.Canny(img, 30, 20)
con, hir = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
new_img = np.zeros((img.shape[0], img.shape[1], 3), dtype='uint8')
print(len(con))

for i in range(len(con)):
    if 0 <= i < len(con) // 2.96:
        color = colors['green']
    elif len(con) // 2.96 <= i < len(con) // 2.96 * 2.16:
        color = colors['red']
    else:
        color = colors['purple']
    cv2.drawContours(new_img, con, i, color, 1, cv2.LINE_8, hir, 0)


cv2.imshow('Result', new_img)
cv2.waitKey(0)
cv2.imwrite('Result_image.jpg', new_img)


