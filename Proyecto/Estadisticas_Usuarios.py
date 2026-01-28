# Número total de usuarios
import Usuarios


total_usuarios = len(Usuarios)

# Lista con solo las edades
edades = []
for u in Usuarios:
    edades.append(u[2])

# Edad media
edad_media = sum(edades) / total_usuarios

# Usuario más joven y más mayor
mas_joven = min(Usuarios, key=lambda x: x[2])
mas_mayor = max(Usuarios, key=lambda x: x[2])

# Mostrar resultados
print("Total de usuarios:", total_usuarios)
print("Edad media:", edad_media)
print("Usuario más joven:", mas_joven)
print("Usuario más mayor:", mas_mayor)
print("\nLista de usuarios:")
for u in Usuarios:
    print(u)