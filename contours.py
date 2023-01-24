import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    _, img = cap.read()
    # detect and decode

    cv2.imshow("original", img)
    if cv2.waitKey(1) == ord("q"):
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edged = cv2.Canny(gray, 30, 200)

    contours, hierarchy = cv2.findContours(edged,
                                           cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.imshow('Canny Edges After Contouring', edged)

    print("Number of Contours found = " + str(len(contours)))

    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

    cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()