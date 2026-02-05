# Lista global de usuarios
usuarios = []

def añadir_usuario():
    id_usuario = input("ID del usuario: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ciudad = input("Ciudad: ")

    usuario = (id_usuario, nombre, edad, ciudad)
    usuarios.append(usuario)

    print("Usuario añadido correctamente")

# Llamamos a la función
añadir_usuario()

# Mostramos la lista
print("Lista de usuarios:")
print(usuarios)
