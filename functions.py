# aqui Creare las funciones y llamare las librerias que sean necesarias para que el Codigo sea Eficiente.
import csv , os
import pandas as pd

def menu_login():

    while True:
        login_df = pd.read_csv('usuarios.csv')
        
        usuario = input('\nEscriba el nombre de usuario: ')
        contraseña = input('\nEscriba la contraseña: ')
        
        match = login_df[(login_df['USUARIO'] == usuario) & (login_df['CONTRASEÑA'] == contraseña)]    
        if not match.empty:
            print("Inicio de sesión exitoso...!")
            
            break
                
        else:
            print('El usuario o la contraseña no son correctos.')
                

def user_contra(login):
    
    while True:
        usuario = input('\nEscriba el nombre de usuario: ')
        contraseña = input('\nEscriba la contraseña: ')
        
        user_ingresado = {"USUARIO": usuario, "CONTRASEÑA": contraseña}
        
        login.append(user_ingresado)
        
        
    
        if os.path.exists('usuarios.csv'):
            #si el archivo existe agrego Append  'A'
            with open('usuarios.csv','a',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['USUARIO','CONTRASEÑA'])
                guardar.writerows(login)        
        else: #Si no existe abro en modo escritura 'W'
            with open('usuarios.csv','w',newline='',encoding='utf-8') as archivo:
                    guardar = csv.DictWriter(archivo,fieldnames=['USUARIO','CONTRASEÑA'])
                    guardar.writeheader()
                    guardar.writerows(login)
                
                
                
                
"""while True:
        try:
            print('\n1. Crear un nuevo usuario. ')
            print('\n2. Cambiar contraseña. ')
            
            opcion_usuario = input('Ingrese el numero de la opción que desee: ')
            
            if opcion_usuario == '1':
                print('El usuario debe tener solo letras')
                user = input('\nIngrese su usuario:')
                
                print('La Contraseña debe ser de al menos 6 Caracteres')
                pasword = input('\nIngrese la contraseña: ') 
        except ValueError:
                print('Error: ingrese los datos correctamente. ')
                continue"""


def consulta(): # esta funcion me ayuda a consultar lo que hay en el archivo csv donde guardo mis datos.
    while True:    
        
        df_inventario = pd.read_csv('ferreteria.csv') # me convierte mi csv a un df para poder trabajarlo.
        
        pd.set_option('display.max_rows', None)  # Para mostrar todas las filas
        pd.set_option('display.max_columns', None)  # Para mostrar todas las columnas
        pd.set_option('display.width', None)  # Para no limitar el ancho
        pd.set_option('display.max_colwidth', None)  # Para no truncar el texto de las columnas
        
        print('\n', df_inventario)
        
        #Consultamos por un articulo en especifico que estemos buscando
        consulta_nombre = str(input('\nIngrese el nombre del articulo que desea consultar: ').upper())
        if consulta_nombre in df_inventario['NOMBRE'].values:
            articulo = df_inventario[df_inventario['NOMBRE'] == consulta_nombre ]
            print(articulo)
            
        else:
            ('El articulo no esta en el inventario.')    
        
        #codigo que nos da la opcion de salir o repetir
        repetir = input('\nDesea consultar otro articulo? S/N : ').upper()
        if repetir == 'S':
            consulta()
        elif repetir == 'N':
            break
        else: 
            print('Ingrese un numero correcto')
            


def salida_inv():
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
            cantidad = int(input('Digite la cantidad que deseea sacar del Sistema: '))
            
        except ValueError:
            print('error: ingrese una opcion valida: ')    
            continue
        
        # toma el nombre ingresado y en caso de estar  en el inventario nos 
        if nombre_art in df_inventario['NOMBRE'].values:
           df_inventario.loc[df_inventario['NOMBRE']==nombre_art,'CANTIDAD'] -= cantidad# resta la cantidad ingresada
        
        else:
            print('\nEl Articulo no se encuentra en sistema: ')
        
        # almacena directamente la nueva cantidad de los articulos
        df_inventario.to_csv('ferreteria.csv')
        print(df_inventario)

        print('\nCambios guardados con exito.')
        
        repetir = input('Desea hacer otra Salida? s/n? : ').upper() # damos la opcion de continuar o salir
        
        if repetir == 'S':
            print('\n---Salida de otro articulo---')
        
        elif repetir == 'N':
            print('Volviendo al menú principal')
            break
        else: 
            print('Ingrese una letra correcta, s/n: ')  
        
        
        
    print(df_inventario)
         
       
def entrada_inv(lista_articulos): # me permite crear una entrada al inventario con lo que se desee ingresar.
    
    df_inventario = pd.read_csv('ferreteria.csv', encoding='utf-8')
    
    pd.set_option('display.max_rows', None)  # Para mostrar todas las filas
    pd.set_option('display.max_columns', None)  # Para mostrar todas las columnas
    pd.set_option('display.width', None)  # Para no limitar el ancho
    pd.set_option('display.max_colwidth', None)  # Para no truncar el texto de las columnas
    
    print(df_inventario)
    
    while True:    
        
        try: # solicito los datos que el usuario quiere ingresar al sistema.
            nombre_art = input('Ingrese el nombre del Articulo: ').upper()
            marca = input('ingrese la Marca del fabricante: ').upper()
            cantidad = int(input('Digite la cantidad que desea ingresar al Sistema: '))
            precio = float(input('Ingrese el Valor del articulo en colones: '))
            
        except ValueError:
                print('El valor no es correcto, por favor intentelo nuevamente!')
                continue    
        
        #tomamos el nombre ingresado y validamos si se encuentra en el inventario
        if nombre_art in df_inventario['NOMBRE'].values: 
            df_inventario.loc[df_inventario['NOMBRE']==nombre_art,'CANTIDAD'] += cantidad #si está en el inventario sumamos la cantidad a la ya existente
            df_inventario.to_csv('ferreteria.csv') # guardamos la modificacion en el archivo csv
            print(df_inventario)
            print('\nInventario Actualizado. ')
        
            # damos la opcion de repetir
            repetir = input('Desea hacer otro ingreso? s/n? : ').upper() # damos la opcion de continuar o salir
            
            if repetir == 'S':
                print('\n---Ingresando otro articulo---')
            
            elif repetir == 'N':
                print('Volviendo al menú principal')
                break
            else: 
                print('Ingrese una letra correcta, s/n: ')

        #en caso de no coincidir el nombre con el brindado, hacemos el ingreso de un nuevo articulo a la variable
        if nombre_art not in df_inventario['NOMBRE'].values[0]: 
            modificacion = {'NOMBRE': nombre_art, 'MARCA': marca, 'CANTIDAD':cantidad, 'PRECIO':precio}
            
            lista_articulos.append(modificacion)
            
            print(modificacion)
            print('\nNo olvides guardar los datos en el menú principal')# en este metodo se necesita usar el guardado del menú principal
            
            repetir = input('Desea hacer otro ingreso? s/n? : ').upper() # damos la opcion de continuar o salir
            if repetir == 'S':
                print('\n---Ingresando otro articulo---')
            
            elif repetir == 'N':
                print('Volviendo al menú principal')
                break
            else: 
                print('Ingrese una letra correcta, s/n: ')       
                            
        
        

def guardar_ingreso(modificacion): # me permite cuardar los datos que se almacenan en las listas ingreso y salida
    if not modificacion:
        print('No hay ingresos que guardar en el CSV')
    else:
        if os.path.exists('ferreteria.csv'):
            #si el archivo existe agrego Append  'A'
            with open('ferreteria.csv','a',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['NOMBRE','MARCA','CANTIDAD','PRECIO'])
                guardar.writerows(modificacion)        
        else: #Si no existe abro en modo escritura 'W'
            with open('ferreteria.csv','w',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['NOMBRE','MARCA','CANTIDAD','PRECIO'])
                guardar.writeheader()
                guardar.writerows(modificacion)
                
        #Limpio las ventas en memoria y muestro el guardado exitoso                
        modificacion = []
        print('Datos guardados exitosamente!') 
        



def analizis_inv(): # utilizando pandas me permite ver algunos datos que pueden ser de relevancia para el usuario.
    while True:
    
        df_inv = pd.read_csv('ferreteria.csv', encoding='utf-8')
        
        print('\nLos articulos con mayor stock son: ')
        print('\n',df_inv[ df_inv['CANTIDAD'] == df_inv['CANTIDAD'].max()]) 
        print('\nLos articulos con menor stock son: ') 
        print('\n',df_inv[df_inv['CANTIDAD'] == df_inv['CANTIDAD'].min()])
        print('\nLos articulos de mayor valor son: ')
        print('\n',df_inv[df_inv['PRECIO'] == df_inv['PRECIO'].max()])
        print('\nLos articulos de menor valor son: ')
        print('\n',df_inv[df_inv['PRECIO'] == df_inv['PRECIO'].min()])
        

        salir = input('\nPara salir digite 1: ')
        
        if salir == '1':
            break
        
        else: 
            print('\nDigite un valor correcto')
    
    