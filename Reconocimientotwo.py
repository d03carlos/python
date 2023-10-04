import cv2
import face_recognition as fr

#foto control
img = fr.load_image_file('pics/011.jpg')
img_test = fr.load_image_file('pics/09.jpg')
#pasar imagen a RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#encontrar rostros
face_locations = fr.face_locations(img)[0]

face_codification = fr.face_encodings(img)[0]
cv2.rectangle(img, (face_locations[3], face_locations[0]),
              (face_locations[1], face_locations[2]),
              (255, 0, 0), 2)
#realizar comparacion
results = fr.compare_faces([face_codification], face_codification)
#mostrar resultado
print(results)

#mostrar imagenes
cv2.imshow('Persona', img)
cv2.imshow('Persona test', img_test)
cv2.waitKey(0)
