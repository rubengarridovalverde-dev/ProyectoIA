# Creamos una lista vacía para guardar los usuarios
usuarios = []

# Pedimos al usuario que introduzca el ID
id_usuario = input("ID del usuario: ")

# Pedimos el nombre del usuario
nombre = input("Nombre: ")

# Pedimos la edad y la convertimos a número entero
edad = int(input("Edad: "))

# Pedimos la ciudad del usuario
ciudad = input("Ciudad: ")

# Creamos una tupla con los datos del usuario
usuario = (id_usuario, nombre, edad, ciudad)

# Añadimos la tupla a la lista de usuarios
usuarios.append(usuario)

# Mostramos un mensaje
print("\nLista de usuarios:")

# Mostramos la lista completa de usuarios
print(usuarios)
