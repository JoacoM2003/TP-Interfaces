import cv2
import random
import SeguimientoManos as sm  # Clase manos
import os
import imutils

start = False
arriba = False
abajo = False
derecha = False
izquierda = False
juego = False
reset = False
botWin = False
userWin = False
draw = False

path = 'Imagenes'
images = []
clases = []
lista = os.listdir(path)

for lis in lista:
    imgdb = cv2.imread(f'{path}/{lis}')
    images.append(imgdb)
    clases.append(os.path.splitext(lis)[0])

cap = cv2.VideoCapture(0)
detector = sm.detectormanos()

while True:
    ret, frame = cap.read()
    teclado = cv2.waitKey(1)

    al, an, c = frame.shape
    cx = int(an / 2)
    cy = int(al / 2)

    frame = cv2.flip(frame, 1)
    frame = detector.encontrarmanos(frame, dibujar=True)
    lista1, bbox1, jug = detector.encontrarposicion(frame, ManoNum=0, dibujar=True, color=[0, 255, 0])

    cv2.line(frame, (cx,0), (cx,480), (0,255,0), 2)

    cv2.rectangle(frame, (245, 25), (380, 60), (0, 0, 0), -1)
    cv2.putText(frame, 'COMIENZA EL JUEGO', (250, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.71,(0, 255, 0), 2)

    cv2.imshow("JUEGO", frame)

    if teclado == 27 or cv2.getWindowProperty("JUEGO", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()

