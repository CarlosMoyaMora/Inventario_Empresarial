# aqui Creare las funciones y llamare las librerias que sean necesarias para que el Codigo sea Eficiente.
import csv , os
import pandas as pd

def salida_inv():
    
    pass




def consulta():
    df_inventario = pd.read_csv('ferreteria.csv', encoding='utf-8')
    print(df_inventario)
    consulta_articulo = input('Ingrese el nombre del articulo que desea consultar: ').upper()
    if consulta_articulo in df_inventario:
        datos_articulo = []
        datos_articulo.append(df_inventario[[consulta_articulo]])
        print(datos_articulo) 
                
        repetir = input('Desea consultar otro articulo? S/N : ').upper()
        if repetir == 'S':
            consulta()
        elif repetir == 'N':
            salida_inv()
        else: 
            print('Ingrese un numero correcto')
        
    


def entrada_inv(lista_articulos):
    while True:    
        
        try:
            nombre_art = input('Ingrese el nombre del Articulo: ').upper()
            marca = input('ingrese la Marca del fabricante: ').upper()
            cantidad = int(input('Digite la cantidad que deseea ingresar al Sistema: '))
            precio = float(input('Ingrese el Valor del articulo: '))
            fecha_ing = input('Ingrese la fecha del ingreso AAAA/MM/DD: ')
        except ValueError:
                print('El valor no es correcto, por favor intentelo nuevamente!')
                continue    
            
        ingreso = {'NOMBRE': nombre_art,'MARCA': marca, 'CANTIDAD' : cantidad, 'PRECIO' : precio, 'FECHA' : fecha_ing} 
        
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
        if os.path.exists('ferreteria.csv'):
            #si el archivo existe agrego Append  'A'
            with open('ferreteria.csv','a',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['NOMBRE','MARCA','CANTIDAD','PRECIO','FECHA'])
                guardar.writerows(ingreso)        
        else: #Si no existe abro en modo escritura 'W'
            with open('ferreteria.csv','w',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['NOMBRE','MARCA','CANTIDAD','PRECIO','FECHA'])
                guardar.writeheader()
                guardar.writerows(ingreso)
                
        #Limpio las ventas en memoria y muestro el guardado exitoso                
        ingreso = []
        print('Datos guardados exitosamente!')        