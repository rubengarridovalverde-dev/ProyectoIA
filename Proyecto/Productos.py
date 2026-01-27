productos={  'manzana':10.6,
           
}

def main():
      
        print(productos)
        modificar_precios()
        print(productos)
        
        
        
def añadir_productos():  
    nombre=str(input("Ingrese el nombre de su producto: "))
    
    precio=int(input("Introduzca el precio: "))
    
    productos[nombre]=precio
   
    
def modificar_precios():
    
    nombre=str(input("Ingrese el nombre de su producto al cual quiera cambiar el precio: "))
    if nombre not in productos:       
        print("Este producto no se encuentra registrado en la base de datos, si quieres agregar use la opcion de añadir productos")
    else:
        precio=int(input("Introduzca el nuevo precio: "))
        productos[nombre]=precio
    
    
    
    
    
    
    
if __name__=="__main__":
    main()

    
    
    
    