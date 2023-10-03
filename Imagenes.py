import cv2

img = cv2.imread("images/contornos.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
umbral = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
contornos, jerarquia = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#dibujar contornos
cv2.drawContours(img, contornos, -1, (0, 255, 0), 3)
#mostrar
cv2.imshow("Imagen original", img)
#cv2.imshow("Output", gray)
#cv2.imshow('Umbral', umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()