# Lista donde se guardan los usuarios
usuarios = []

# -------- CREAR USUARIO --------
def añadir_usuario():
    id_usuario = input("ID del usuario: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ciudad = input("Ciudad: ")

    usuario = (id_usuario, nombre, edad, ciudad)
    usuarios.append(usuario)

    print("Usuario añadido correctamente\n")


# -------- ESTADÍSTICAS --------
def estadisticas_usuarios():
    if len(usuarios) == 0:
        print("No hay usuarios registrados\n")
        return

    total = len(usuarios)

    suma_edades = 0
    for u in usuarios:
        suma_edades += u[2]

    edad_media = suma_edades / total

    mas_joven = min(usuarios, key=lambda x: x[2])
    mas_mayor = max(usuarios, key=lambda x: x[2])

    print("Total de usuarios:", total)
    print("Edad media:", edad_media)
    print("Usuario más joven:", mas_joven)
    print("Usuario más mayor:", mas_mayor)
    print()


# -------- MENÚ --------
while True:
    print("""
MENÚ
1. Añadir usuario
2. Estadísticas de usuarios
3. Salir
""")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        añadir_usuario()
    elif opcion == "2":
        estadisticas_usuarios()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida\n")
# Fin del programa