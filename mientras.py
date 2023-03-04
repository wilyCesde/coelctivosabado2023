
controladora = 100

print("***Empanadas el machetico***")
print("****************************")
print("1.Agragregar sabor de enpanada")
print("1.mostrar sabor de empanada")
print("1.cambiar sabor de empanada")
print("0.Salir")

while (controladora != 0):
    empanada = None
    controladora = int(input("digita una opcion: "))
    if controladora == 1:
        empanada = input("cual es el sabor")
    elif controladora == 2:
        empanada = input("el sabor es {empanada}")

    elif controladora == 3:
        empanada = input("cual es el sabor:")

    elif controladora == 0:
        empanada = input("cual es el sabor")
    else:
        empanada = input("opcion invalida")
