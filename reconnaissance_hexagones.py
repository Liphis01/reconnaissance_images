import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Parametres optimaux a determiner
nbrMatches = 25
thresh = 25
couleurs = ["rouge", "vert", "bleu", "orange"]

# Recuperation des images de chaque hexagone
imgs = [cv.imread('images/' + str(c) + '_2.png', cv.IMREAD_GRAYSCALE) for c in couleurs]

# Flux video
cap = cv.VideoCapture(0, cv.CAP_DSHOW)

def photo(nom_image):
    if cv.waitKey(1) == ord("p"):
        cv.imwrite('images/'+nom_image+'.png', image)
        print("photo")

def affichage():
    # Affichage des distances de chaque hexagone
    for i in range(len(matches)):
        cv.putText(img, str(int(matches[i][-1].distance)), (550, 50 + 75 * i), cv.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255),
                   2, cv.LINE_AA)
    # Detection des hexagones qui se trouvent dans l'image
    hexas = [i for i in range(len(matches)) if matches[i][-1].distance < thresh]
    # Triage selon la distance de leur dernier match
    hexas = sorted(hexas, key=lambda j: int(matches[j][-1].distance))
    # Affichage
    for i in hexas:
        cv.putText(img, couleurs[i].upper(), (5, 50 + 75 * i), cv.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2, cv.LINE_AA)

while True:
    _, image = cap.read()
    img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    if cv.waitKey(1) == ord("q"):
        break

    photo("orange_2")

    # Initialisation du detecteur ORB
    orb = cv.ORB_create()
    # Recherche des keypoints et descriptors avec ORB
    kp, des = [], []
    for i in range(len(imgs)):
        a, b = orb.detectAndCompute(imgs[i], None)
        kp.append(a); des.append(b)
    kp_cap, des_cap = orb.detectAndCompute(img, None)

    # creation d'objets BFMatcher
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

    try:
        # Match entre les descriptors pour chaque hexagone.
        matches = [bf.match(x, des_cap) for x in des]
        # Triage des matches selon leur distance.
        matches = [sorted(m, key=lambda x: x.distance)[:nbrMatches] for m in matches]
        # Draw first matches.
        #img3 = cv.drawMatches(img1, kp1, img2, kp2, matches[:nbrMatches], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

        affichage()
        cv.imshow("Hex_recognition", img)
    except cv.error: pass #print("erreur")

cv.waitKey(0)
cv.destroyAllWindows()