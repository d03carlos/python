#funcion suma
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "Error"
    return a/b
print(suma(2,3))
print(resta(2,3))
print(multiplicacion(2,3))
print(division(2,1))