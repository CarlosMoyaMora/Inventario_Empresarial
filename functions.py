# aqui Creare las funciones y llamare las librerias que sean necesarias para que el Codigo sea Eficiente.


def salida_inv():
    
    pass




def consulta():
    pass


def entrada_inv(nuevo_ingreso):
    while True:    
        
        try:
            nombre_art = input('Ingrese el nombre del Articulo: ')
            cantidad = int(input('Digite la cantidad que deseea ingresar al Sistema: '))
            precio = float(input('Ingrese el Valor del articulo: '))
            fecha_ing = input('Ingrese la fecha del ingreso: ')
        except ValueError:
                print('El valor no es correcto, por favor intentelo nuevamente!')
                continue    
            
        ingreso = {'nombre': nombre_art, 'cantidad' : cantidad, 'precio' : precio, 'fecha' : fecha_ing} 
        
        nuevo_ingreso.append(ingreso)
       