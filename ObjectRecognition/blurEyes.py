import cv2

cap = cv2.VideoCapture(0)


while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes_cascade = cv2.CascadeClassifier('eyes.xml')

    eyes = eyes_cascade.detectMultiScale(gray, scaleFactor=1.7, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in eyes:
        square = cv2.rectangle(img.copy(), (x - 30, y), (x + w + 30, y + h), (150, 150, 150), thickness=-1)
        cv2.blur(square.copy(), (15, 15))
        img = cv2.bitwise_and(img, square)

    cv2.imshow("Сamera", img)

    if cv2.waitKey(1) == 27:  # Клавиша Esc
        break

cap.release()
cv2.destroyAllWindows()
cv2.imwrite("image_eye_1.jpg", img)