import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    _, image = cap.read()
    cv2.putText(image, "Match", (5, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("Rectified QRCode", image)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()