class MyClase:
    def __init__(self, name, apellido):
        self.name = name
        self.apellido = apellido

    def saludar(self):
        print(f"Hola {self.name} {self.apellido}")
persona1 = MyClase("Hella", "Gutierrez") 
persona1.saludar()