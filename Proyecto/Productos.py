productos={
}

def main():
    print("Menú interactivo")
    print
        
        
def añadir_productos():  
    nombre=str(input("Ingrese el nombre de su producto: "))
    if nombre in productos:
        print("Este producto ya se encuentra en la base de datos, si desea eliminar o modificar precio use la opcion correspondiente")
    else: 
        precio=int(input("Introduzca el precio: "))
        productos[nombre]=precio
   
    
def modificar_precios():  
    nombre=str(input("Ingrese el nombre de su producto al cual quiera cambiar el precio: "))
    if nombre not in productos:       
        print("Este producto no se encuentra registrado en la base de datos, si quieres agregar use la opcion de añadir productos")
    else:
        precio=int(input("Introduzca el nuevo precio: "))
        productos[nombre]=precio
    
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

    
    
    
    