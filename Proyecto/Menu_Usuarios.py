print("MENÚ DE ESTADÍSTICAS")
import Usuarios

print("1. Número total de usuarios")
print("2. Edad media")
print("3. Usuario más joven y más mayor")

opcion = input("Elige una opción: ")

if opcion == "1":
    print("Total de usuarios:", len(Usuarios))

elif opcion == "2":
    suma_edades = 0
    for u in Usuarios:
        suma_edades += u[2]
    edad_media = suma_edades / len(Usuarios)
    print("Edad media:", edad_media)

elif opcion == "3":
    mas_joven = min(Usuarios, key=lambda x: x[2])
    mas_mayor = max(Usuarios, key=lambda x: x[2])
    print("Usuario más joven:", mas_joven)
    print("Usuario más mayor:", mas_mayor)

else:
    print("Opción no válida")
