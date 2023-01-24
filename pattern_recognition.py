import cv2
import numpy as np


cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_COMPLEX                ##Font style for writing text on video frame
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)        ##Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

x1 = 750        ##450
x2 = 930        ##630
y1 = 100
y2 = 300

Result_Count1 = 0
Result_Count2 = 0
Result_Count3 = 0
Result_Count4 = 0

Pattern_Matrix = np.zeros((8, 8), np.uint8)

Pattern_1 = np.flip(np.array([  [1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 0, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 1, 1, 0, 0, 1],
                                [1, 0, 0, 1, 1, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 0, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1]
                                ], dtype=np.uint8), axis=1) * 255

Pattern_2 = np.flip(np.array([  [1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 0, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 1, 0, 0, 0, 1],
                                [1, 0, 1, 0, 1, 1, 0, 1],
                                [1, 0, 0, 1, 1, 0, 0, 1],
                                [1, 0, 0, 1, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 0, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1]
                                ], dtype=np.uint8), axis=1) * 255

Pattern_3 = np.flip(np.array([  [1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 0, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 1, 0, 1],
                                [1, 0, 1, 0, 0, 0, 0, 1],
                                [1, 0, 0, 1, 1, 1, 0, 1],
                                [1, 0, 0, 1, 0, 1, 0, 1],
                                [1, 0, 0, 0, 0, 0, 0, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1]
                                ], dtype=np.uint8), axis=1) * 255

Pattern_4 = np.flip(np.array([  [1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 0, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 1, 0, 0, 1],
                                [1, 0, 1, 0, 1, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 0, 1],
                                [1, 0, 1, 1, 1, 1, 0, 1],
                                [1, 0, 0, 0, 0, 0, 0, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1]
                                ], dtype=np.uint8), axis=1) * 255

while 1:
    ret, frame = cap.read()         ##Read image frame
    frame = cv2.flip(frame, +1)     ##Mirror image frame

    if not ret:                     ##If frame is not read then exit
        break
    if cv2.waitKey(1) == ord('s') or cv2.waitKey(1) == ord('S'):  ##While loop exit condition
        break

    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', frame2)

    ret, thresh1 = cv2.threshold(frame2, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binary Image', thresh1)

    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    width = int((x2-x1)/8)
    height = int((y2-y1)/8)
    W1 = x1
    H1 = y1
    W2 = x1 + width
    H2 = y1 + height

    for i in range(0, 8):
        for j in range(0, 8):
            Sum = np.sum(thresh1[H1: H2, W1:W2])                    ##56100
            if Sum > 56100:
                Pattern_Matrix[i, j] = 255
            else:
                Pattern_Matrix[i, j] = 0
            W1 = W2
            W2 = W2 + width
            #print('W1 = ' +str(W1))
            #print('W2 = ' +str(W2))
            #print('H1 = ' +str(H1))
            #print('H2 = ' +str(H2))
            #print("Sum = "+str(Sum))
            Sum = 0
        W1 = x1
        W2 = x1 + width
        H1 = H2
        H2 = H2 + height


    #print(Pattern_Matrix)
    #print("width="+str(width))
    #print("height="+str(height))



    ##*******************Pattern Comparison*********************##

    for a in range(0, 8):
        for b in range (0, 8):
            if Pattern_Matrix[a, b] == Pattern_1[a, b]:
                Result_Count1 = Result_Count1 + 1
            if Pattern_Matrix[a, b] == Pattern_2[a, b]:
                Result_Count2 = Result_Count2 + 1
            if Pattern_Matrix[a, b] == Pattern_3[a, b]:
                Result_Count3 = Result_Count3 + 1
            if Pattern_Matrix[a, b] == Pattern_4[a, b]:
                Result_Count4 = Result_Count4 + 1

    ##print(Result_Count)

    Match_Percentage1 = (Result_Count1 / 64) * 100
    Match_Percentage2 = (Result_Count2 / 64) * 100
    Match_Percentage3 = (Result_Count3 / 64) * 100
    Match_Percentage4 = (Result_Count4 / 64) * 100

    Result_Count1 = 0
    Result_Count2 = 0
    Result_Count3 = 0
    Result_Count4 = 0

    if Match_Percentage1 > 90:
        S = "Pattern 1  " + str(round(Match_Percentage1, 1)) + '%'
        cv2.putText(frame, S, (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
    elif Match_Percentage2 > 90:
        S = "Pattern 2  " + str(round(Match_Percentage2, 1)) + '%'
        cv2.putText(frame, S, (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
    elif Match_Percentage3 > 90:
        S = "Pattern 3  " + str(round(Match_Percentage3, 1)) + '%'
        cv2.putText(frame, S, (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
    elif Match_Percentage4 > 90:
        S = "Pattern 4  " + str(round(Match_Percentage4, 1)) + '%'
        cv2.putText(frame, S, (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
    else:
        cv2.putText(frame, "No Match Found", (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Original Image', frame)
    cv2.imshow('Pattern Template', thresh1[y1:y2, x1:x2])