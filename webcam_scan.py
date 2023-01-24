import cv2
import numpy as np
import sys
import time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)

    # Display results
    cv2.imshow("Results", im)

while True:
    _, img = cap.read()
    # detect and decode
    data, bbox, rectifiedImage = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if data:
        a=data
        break

    cv2.imshow("QRCODEscanner", img)
    if cv2.waitKey(1) == ord("q"):
        break

#t = time.time()
#print("Time Taken for Detect and Decode : {:.3f} seconds".format(time.time() - t))
if len(data)>0:
    print("Decoded Data : {}".format(data))
    display(img, bbox)
    rectifiedImage = np.uint8(rectifiedImage);
    cv2.imshow("Rectified QRCode", rectifiedImage);
else:
    print("QR Code not detected")
    cv2.imshow("Results", img)
cv2.imwrite("output.jpg",img)
cv2.imwrite("QRcode.jpg", rectifiedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
