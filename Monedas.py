import cv2
import numpy as np
#varGauss = 3
#varKernel = 3
original = cv2.imread('images/monedas.jpg')

gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(gray, (5, 5), 0)
canny = cv2.Canny(gauss, 50, 150)
inicio = np.ones((5, 5), np.uint8)
cierre = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, inicio)
contornos, jerarquia = cv2.findContours(cierre.copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('monedas encontradas: ', len(contornos))
cv2.imshow('gray', gray)
cv2.imshow('gauss', gauss)
cv2.imshow('cierre', cierre)
cv2.waitKey(0)
