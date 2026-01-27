productos={
}



def main():
    seleccionador=0
    menu=True

    while menu:
        print("Menú interactivo")
        print("_______________________")
        print("1. Añadir Usuarios")
        print("2. Mostrar Usuarios")
        print("3. Añadir Producto")
        print("4. Mostrar Productos")
        print("5. Estadisticas")
        print("6. Busquedas")
        print("7. Salir")

        seleccionador=int(input("Introduzca numero asociado a la accion que quiere hacer: "))


        if seleccionador == 1:
            print("Funcion 1")    
        elif seleccionador==2:
            print("Funcion 2")
        elif seleccionador==3:
            añadir_productos()
        elif seleccionador==4:
            mostrar_catalogo()
        elif seleccionador==5:
            print("Funcion 5")
        elif seleccionador==6:
            print("Funcion 6")
        elif seleccionador==7:
            print("Gracias por usar nuestra aplicacion")
            menu=False
        else:
            print("Opcion no asociada a ninguna accion")
    
        
def añadir_productos():  
    nombre=str(input("Ingrese el nombre de su producto: "))
    if nombre in productos:
        print("Este producto ya se encuentra en la base de datos, si desea eliminar o modificar precio use la opcion correspondiente")
    else: 
        try:
            precio_cadena=str(input("Introduzca el precio: "))
            precio_numero=float(precio_cadena) #esto convierte a float una cadena ya que no existe variables double en python
            productos[nombre]=precio_numero #aln convertirlo podemos comprobar si el precio es numerico 
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

    
    
    
    