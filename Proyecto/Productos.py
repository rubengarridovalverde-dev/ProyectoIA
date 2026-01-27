productos={
}

def main():
    print("Menú interactivo")
    print
    añadir_productos()
        
        
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

    
    
    
    