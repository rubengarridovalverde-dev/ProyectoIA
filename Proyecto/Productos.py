productos={
}

menu=True

def main():
    global menu #boolean creado para poder cerrar el programa
    opcion=0
    while menu:
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
            seleccionador(opcion)
            if opcion ==7: menu=False
        except ValueError:
            print("No has metido un precio en formato numerico")
       
   

        
    
def seleccionador(numero):
    if numero == 1:
        print("Funcion 1")    
    elif numero==2:
        print("Funcion 2")
    elif numero==3:
        submenu_productos()      
    elif numero==4:
        mostrar_catalogo()
    elif numero==5:
        print("Funcion 5")
    elif numero==6:
        print("Funcion 6")
    elif numero==7:
        print("Gracias por usar nuestra aplicacion")
    else:
        print("Opcion no asociada a ninguna accion")


def submenu_productos():
    print("Modificar Productos")
    print("_______________________")
    print("1. Añadir Productos")
    print("2. Eliminar Productos")
    print("3. Modificar Precios")

    try:
        opcion_productos=int(input("Introduzca numero asociado a la accion que quiere hacer: "))
        seleccionador_productos(opcion_productos)
    except ValueError:
        print("No has metido un precio en formato numerico")
 
 
       
def seleccionador_productos(opcion):
        
    if opcion==1:
        añadir_productos()
    elif opcion==2:
        eliminar_productos()
    elif opcion==3:
        modificar_precios()



def añadir_productos():  
    nombre=str(input("Ingrese el nombre de su producto: "))
    if nombre in productos:
        print("Este producto ya se encuentra en la base de datos, si desea eliminar o modificar precio use la opcion correspondiente")
    else: 
        try:
            precio_cadena=str(input("Introduzca el precio: "))
            precio_numero=float(precio_cadena) #esto convierte a float una cadena ya que no existe variables double en python
            productos[nombre]=precio_numero #al convertirlo podemos comprobar si el precio es numerico 
        except ValueError:
            print("No has metido un precio en formato numerico")
       
   
    
def modificar_precios():  
    nombre=str(input("Ingrese el nombre de su producto al cual quiera cambiar el precio: "))
    if nombre not in productos:       
        print("Este producto no se encuentra registrado en la base de datos, si quieres agregar use la opcion de añadir productos")
    else:
        try:
            precio_cadena=str(input("Introduzca el nuevo precio: "))
            precio_numero=float(precio_cadena) 
            productos[nombre]=precio_numero 
        except ValueError:
            print("No has metido un precio en formato numerico")
    
def eliminar_productos():
    nombre=str(input("Ingrese el nombre del producto a eliminar: "))
    if nombre not in productos:
        print("Este producto no se encuentra registrado en la base de datos")
    else:
        del productos[nombre]
    
def mostrar_catalogo():
    print(productos)
    
    
if __name__=="__main__":
    main()

    
    
    
    