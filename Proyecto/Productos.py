productos={  
}

def main():
    while(True):
        añadir_productos()
        print(productos)
        
        
        
def añadir_productos():  
    nombre=str(input("Ingrese el nombre de su producto: "))
    
    precio=int(input("Introduzca el precio: "))
    
    productos[nombre]=precio
   
    
    
    
if __name__=="__main__":
    main()

    
    
    
    