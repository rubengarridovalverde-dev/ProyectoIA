# Buscar usuarios por ciudad
import Usuarios

def buscar_por_ciudad():
    ciudad = input("Introduce la ciudad a buscar: ")
    encontrados = [u for u in Usuarios if u[3].lower() == ciudad.lower()]

    if encontrados:
        print(f"Usuarios en {ciudad}:")
        for u in encontrados:
            print(f"ID: {u[0]}, Nombre: {u[1]}, Edad: {u[2]}")
    else:
        print(f"No hay usuarios en {ciudad}")
    print()


# Comprobar si un usuario existe por su ID
def comprobar_usuario():
    id_buscar = input("Introduce el ID del usuario: ")
    for u in Usuarios:
        if u[0] == id_buscar:
            print("✅ El usuario existe:")
            print(f"ID: {u[0]}, Nombre: {u[1]}, Edad: {u[2]}, Ciudad: {u[3]}\n")
            return
    print("❌ El usuario no existe\n")
# Fin de Busquedas_usuarios.py