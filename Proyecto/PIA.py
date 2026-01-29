productos={} #dicionario que almacena los productos
usuarios = [] #lista que guarda las duplas de usuarios


def main():
    menu=True #boolean creado para poder cerrar el programa
    #menu principal en el que se expresa todas las posibilidades
    opcion=0
    while menu:
        print("")
        print("Menú interactivo")
        print("_______________________")
        print("1. Añadir Usuarios")
        print("2. Mostrar Usuarios")
        print("3. Modificar Productos")
        print("4. Mostrar Productos")
        print("5. Estadisticas")
        print("6. Busquedas")
        print("7. Salir")
        try:
            opcion=int(input("Introduzca numero asociado a la accion que quiere hacer: "))
            print("")
            seleccionador(opcion)
            if opcion ==7: menu=False
        except ValueError:
            print("No has metido un numero")
       
   

           
def seleccionador(numero):
    #selector principal del menu donde se indica cada accion
    if numero == 1:
        añadir_usuario()
    elif numero==2:
       mostrar_usuarios()
    elif numero==3:
        submenu_productos()      
    elif numero==4:
        mostrar_catalogo()
    elif numero==5:
        estadisticas()
    elif numero==6:
        submenu_busquedas()
    elif numero==7:
        print("Gracias por usar nuestra aplicacion")
    else:
        print("Opcion no asociada a ninguna accion")



def submenu_productos():
    #submenu del apartado modificar productos
    submenu=True
    while submenu:
        print("")
        print("Modificar Productos")
        print("_______________________")
        print("1. Añadir productos")
        print("2. Eliminar productos")
        print("3. Modificar precios")
        print("4. Volver al menu principal")
        try:
            opcion_productos=int(input("Introduzca numero asociado a la accion que quiere hacer: "))
            print("")
            seleccionador_productos(opcion_productos)
            if opcion_productos == 4: submenu=False #boolean con funcion de cerrar el submenu de productos
        except ValueError:
            print("No has metido un numero")



def seleccionador_productos(opcion):
    #aqui se comprueba que hacer en cada opcion del submenu de productos
    if opcion==1:
        añadir_productos()
    elif opcion==2:
        eliminar_productos()
    elif opcion==3:
        modificar_precios()
    elif opcion==4:
        print("")
    else:
        print("Opcion no asociada a ninguna accion")



def submenu_busquedas():
    #submenu de la opcion de busqueda 
    submenu=True
    while submenu:
        print("")
        print("Busquedas y filtrados")
        print("_______________________")
        print("1. Buscar usuarios por ciudad")
        print("2. Comprobar si existe usuario asociado a ID")
        print("3. Volver al menu principal")
        try:
            opcion_busqueda=int(input("Introduzca numero asociado a la accion que quiere hacer: "))
            print("")
            seleccionador_busqueda(opcion_busqueda)
            if opcion_busqueda == 3: submenu=False #este boolean sirve para cerrar el submenu
        except ValueError:
            print("No has metido un numero")
 


def seleccionador_busqueda(opcion):
     #aqui se comprueba que hacer cada opcion del submenu busqueda
    if opcion==1:
        buscar_por_ciudad()
    elif opcion==2:
        comprobar_usuario()
    elif opcion==3:
        print("")
    else:
        print("Opcion no asociada a ninguna accion")



def añadir_usuario():  
    #metodo para añadir usuarios
    try: #try para que la edad se introduzca numerica
        id_usuario = input("ID del usuario: ")
        for u in usuarios: #aqui uso el mismo bucle que en buscar usuario por id para que no se creen dos con el mismo id
            if u[0] == id_usuario:
                print("El id ya se encuentra asociado")
                return
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        if edad > 0:     #comprobacion de que el usuario no tenga edad negativa     
            ciudad = input("Ciudad: ")
            usuario = (id_usuario, nombre, edad, ciudad)
            usuarios.append(usuario)
            print("")
            print("Usuario añadido correctamente")
        else: print("No puedes tener una edad negativa")
    except ValueError:
        print("Error, la edad introducida no es un numero")
    


def mostrar_usuarios():
    if not usuarios: #este if hace que si no hay informacion en la base de datos sobre usuarios lo indique
        print("No hay usuarios registrados")
    else:
        print("Lista de usuarios:")
        print(usuarios)



def estadisticas():
    #este metodo calcula las estadisticas pedidas
    if len(usuarios) == 0: #comprueba si hay usuarios o productos, ya que sin ellos no se pueden hacer las estadisticas
        print("No hay usuarios registrados\n")
        return
    elif not productos:
        print("No hay productos registrados")
    else:
        total = len(usuarios)

        suma_edades = 0
        for u in usuarios:
            suma_edades += u[2]

        edad_media = suma_edades / total

        mas_joven = min(usuarios, key=lambda x: x[2])
        mas_mayor = max(usuarios, key=lambda x: x[2])
        
        media = sum(productos.values()) / len(productos)
        
        print("Total de usuarios:", total)
        print("Edad media:", edad_media)
        print("Usuario más joven:", mas_joven)
        print("Usuario más mayor:", mas_mayor)
        print("Numero Total de productos",len(productos))
        print("Precio medio de los productos",media)
        print()



def añadir_productos():  
    #metodo para añadir productos al diccionario
    nombre=str(input("Ingrese el nombre de su producto: "))
    if nombre in productos: #detecta si hay un producto creado con el mismo nombre
        print("Este producto ya se encuentra en la base de datos, si desea eliminar o modificar precio use la opcion correspondiente")
       
    else: 
        try:
            precio_cadena=str(input("Introduzca el precio: "))
            precio_numero=float(precio_cadena) #esto convierte a float una cadena ya que no existe variables double en python
            if precio_numero > 0: #comprueba que no se introduzca un precio negativo
                productos[nombre]=precio_numero #al convertirlo podemos comprobar si el precio es numerico 
                print("Producto añadido")
            else: print("No se pueden poner precios con valor negativo")
        except ValueError:
            print("No has metido un precio en formato numerico")


    
def modificar_precios(): 
    if not productos: 
        print("No hay productos registrados")
    else: 
        print("Productos disponibles a modificar") #muestra todos los productos disponibles a modificacion
        mostrar_catalogo()
        nombre=str(input("Ingrese el nombre de su producto al cual quiera cambiar el precio: "))
        if nombre not in productos:    #esto detecta si el producto que se quiere modificar existe en la base  
            print("Este producto no se encuentra registrado en la base de datos, si quieres agregar use la opcion de añadir productos")
        else:
            try:
                precio_cadena=str(input("Introduzca el nuevo precio: "))               
                precio_numero=float(precio_cadena) #esto convierte a float una cadena ya que no existe variables double en python
                if precio_numero > 0: #comprobamos que no haya numero negativo
                    productos[nombre]=precio_numero #al convertirlo podemos comprobar si el precio es numerico 
                    print("Precio modificado")
                else: print("No se pueden poner precios con valor negativo")           
            except ValueError:
                print("No has metido un precio en formato numerico")
    


def eliminar_productos():
    if not productos: 
        print("No hay productos registrados") 
    else:
        print("Productos disponibles a modificar") #muestra todos los productos disponibles a eliminacion
        mostrar_catalogo()
        nombre=str(input("Ingrese el nombre del producto a eliminar: "))
        if nombre not in productos:
            print("Este producto no se encuentra registrado en la base de datos")
        else:
            del productos[nombre]
            print("Producto eliminado")
    


def mostrar_catalogo():
    if not productos: #este if hace que si no hay informacion en la base de datos sobre productos lo indique
        print("No hay productos que mostrar")
    else: print(productos)
  
def buscar_por_ciudad():
    # Buscar a los usuarios por ciudad
    ciudad = input("Introduce la ciudad a buscar: ")
    encontrados = [u for u in usuarios if u[3].lower() == ciudad.lower()]

    if encontrados:
        print(f"Usuarios en {ciudad}:")
        for u in encontrados:
            print(f"ID: {u[0]}, Nombre: {u[1]}, Edad: {u[2]}")
    else:
        print(f"No hay usuarios en {ciudad}")
    print()



def comprobar_usuario():
    # Comprobar si un usuario existe por su ID
    id_buscar = input("Introduce el ID del usuario: ")
    for u in usuarios:
        if u[0] == id_buscar:
            print("El usuario existe:")
            print(f"ID: {u[0]}, Nombre: {u[1]}, Edad: {u[2]}, Ciudad: {u[3]}\n")
        else: 
            print("El usuario no existe\n")  
    
if __name__=="__main__":
    main() 