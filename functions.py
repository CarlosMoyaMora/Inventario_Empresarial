# aqui Creare las funciones y llamare las librerias que sean necesarias para que el Codigo sea Eficiente.
import csv , os
import pandas as pd

def salida_inv():
    
    pass




def consulta():
    df = pd.read_csv('inventario ferreteria.csv', encoding='utf-8')
    print(df)
    volver = input('Desea volver al menu principal? : ')
    if volver == 's':
        break
    elif volver == 'n':
        
    


def entrada_inv(lista_articulos):
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
        
        lista_articulos.append(ingreso)
        
        repetir = input('Desea hacer otro ingreso? s/n? : ').upper()
        
        if repetir == 'S':
            print('\n---Ingresando otro articulo---')
        
        elif repetir == 'N':
            print('Volviendo al menu principal')
            break
        else: 
            print('Ingrese una letra correcta, s/n: ')
    
    print(ingreso)            
        
        

def guardar_ingreso(ingreso):
    if not ingreso:
        print('No hay ingresos que guardar en el CSV')
    else:
        if os.path.exists('inventario ferreteria.csv'):
            #si el archivo existe agrego Append  'A'
            with open('inventario ferreteria.csv','a',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['nombre','cantidad','precio','fecha'])
                guardar.writerows(ingreso)        
        else: #Si no existe abro en modo escritura 'W'
            with open('inventario ferreteria.csv','w',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['nombre','cantidad','precio','fecha'])
                guardar.writeheader()
                guardar.writerows(ingreso)
                
        #Limpio las ventas en memoria y muestro el guardado exitoso                
        ingreso = []
        print('Datos guardados exitosamente!')        