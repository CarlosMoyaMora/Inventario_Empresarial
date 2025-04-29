# aqui Creare las funciones y llamare las librerias que sean necesarias para que el Codigo sea Eficiente.
import csv , os
import pandas as pd






def consulta(): # esta funcion me ayuda a consultar lo que hay en el archivo csv donde guardo mis datos.
    while True:    
        
        df_inventario = pd.read_csv('ferreteria.csv') # me convierte mi csv a un df para poder trabajarlo.
        
        pd.set_option('display.max_rows', None)  # Para mostrar todas las filas
        pd.set_option('display.max_columns', None)  # Para mostrar todas las columnas
        pd.set_option('display.width', None)  # Para no limitar el ancho
        pd.set_option('display.max_colwidth', None)  # Para no truncar el texto de las columnas
        
        print('\n', df_inventario)
        
        consulta_nombre = str(input('\nIngrese el nombre del articulo que desea consultar: ').upper())
        if consulta_nombre in df_inventario['NOMBRE'].values:
            articulo = df_inventario[df_inventario['NOMBRE'] == consulta_nombre ]
            print(articulo)
            
        else:
            ('El articulo no esta en el inventario.')    
        
        repetir = input('\nDesea consultar otro articulo? S/N : ').upper()
        if repetir == 'S':
            consulta()
        elif repetir == 'N':
            break
        else: 
            print('Ingrese un numero correcto')
            


def salida_inv(lista_articulos):
    df_inventario = pd.read_csv('ferreteria.csv', encoding='utf-8')
    
    pd.set_option('display.max_rows', None)  # Para mostrar todas las filas
    pd.set_option('display.max_columns', None)  # Para mostrar todas las columnas
    pd.set_option('display.width', None)  # Para no limitar el ancho
    pd.set_option('display.max_colwidth', None)  # Para no truncar el texto de las columnas
    
    print(df_inventario)
    
    while True:
        try:
            nombre_art = input('Ingrese el nombre del Articulo: ').upper()
            marca = input('ingrese la Marca del fabricante: ').upper()
            cantidad = int(input('Digite la cantidad que deseea ingresar al Sistema: '))
            precio = float(input('Ingrese el Valor del articulo: '))
            fecha_ing = input('Ingrese la fecha del ingreso AAAA/MM/DD: ')
        except ValueError:
            print('error: ingrese una opcion valida: ')    
            continue
        
        modificacion = {'NOMBRE': nombre_art,'MARCA': marca, 'CANTIDAD' : cantidad, 'PRECIO' : precio, 'FECHA' : fecha_ing}
        
        lista_articulos.append(modificacion)
        
        repetir = input('Desea hacer otra Salida? s/n? : ').upper() # damos la opcion de continuar o salir
        
        if repetir == 'S':
            print('\n---Salida de otro articulo---')
        
        elif repetir == 'N':
            print('Volviendo al menu principal')
            break
        else: 
            print('Ingrese una letra correcta, s/n: ')  
        
        
        
    print(modificacion)
         
       
def entrada_inv(lista_articulos): # me permite crear una entrada al inventario con lo que se desee ingresar.
    while True:    
        
        try: # solicito los datos que el usuario quiere ingresar al sistema.
            nombre_art = input('Ingrese el nombre del Articulo: ').upper()
            marca = input('ingrese la Marca del fabricante: ').upper()
            cantidad = int(input('Digite la cantidad que deseea ingresar al Sistema: '))
            precio = float(input('Ingrese el Valor del articulo: '))
            fecha_ing = input('Ingrese la fecha del ingreso AAAA/MM/DD: ')
        except ValueError:
                print('El valor no es correcto, por favor intentelo nuevamente!')
                continue    
            
        modificacion = {'NOMBRE': nombre_art,'MARCA': marca, 'CANTIDAD' : cantidad, 'PRECIO' : precio, 'FECHA' : fecha_ing} 
        
        lista_articulos.append(modificacion)# almacena los datos en un diccionario 
        
        repetir = input('Desea hacer otro ingreso? s/n? : ').upper() # damos la opcion de continuar o salir
        
        if repetir == 'S':
            print('\n---Ingresando otro articulo---')
        
        elif repetir == 'N':
            print('Volviendo al menu principal')
            break
        else: 
            print('Ingrese una letra correcta, s/n: ')
    
    print(modificacion)            
        
        

def guardar_ingreso(modificacion): # me permite cuardar los datos que se almacenan en las listas ingreso y salida
    if not modificacion:
        print('No hay ingresos que guardar en el CSV')
    else:
        if os.path.exists('ferreteria.csv'):
            #si el archivo existe agrego Append  'A'
            with open('ferreteria.csv','a',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['NOMBRE','MARCA','CANTIDAD','PRECIO','FECHA'])
                guardar.writerows(modificacion)        
        else: #Si no existe abro en modo escritura 'W'
            with open('ferreteria.csv','w',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['NOMBRE','MARCA','CANTIDAD','PRECIO','FECHA'])
                guardar.writeheader()
                guardar.writerows(modificacion)
                
        #Limpio las ventas en memoria y muestro el guardado exitoso                
        modificacion = []
        print('Datos guardados exitosamente!') 
        
def analizis_inv():
    df_inv = pd.read_csv('ferreteria.csv', encoding='utf-8')
    df_inv = 