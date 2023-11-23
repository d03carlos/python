#Asegúrate de tenerla instalada antes de continuar, 
# puedes hacerlo ejecutando pip install PyPDF2.
import os
from PyPDF2 import PdfReader, PdfWriter
#ruta de la carpeta que contiene los archivos PDF
folder_path = "D:/PDF"
#contraseña para los archivos PDF
password = "456jenifer456a"
#Iterar a través de los archivos PDF en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        #ruta del archivo PDF
        file_path = os.path.join(folder_path, filename)
        #leer el archivo PDF
        reader = PdfReader(file_path)
        #crear un nuevo archivo PDF
        writer = PdfWriter()
        #iterar a través de las páginas del archivo PDF
        for page in reader.pages:
            #agregar la página al nuevo archivo PDF
            writer.add_page(page)
        #escribir el nuevo archivo PDF
        writer.encrypt(password)
        with open(file_path, "wb") as f:
            writer.write(f)
        print(f"El archivo {filename} se ha cifrado correctamente.")
    else:
        print(f"El archivo {filename} no es un archivo PDF.")
        