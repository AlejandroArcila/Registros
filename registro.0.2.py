file = open('registro.txt', 'w')
nombre=input("Introduce tu nombre ")
file.write("Nombre: " + nombre + '\n')
file.close()
