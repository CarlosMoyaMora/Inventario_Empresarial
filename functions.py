# aqui Creare las funciones y llamare las librerias que sean necesarias para que el Codigo sea Eficiente.
import csv , os, emoji
import tkinter as tk
from colorama import init,Fore,Back, Style
import pandas as pd
from pathlib import Path
import tkinter as tk
from tkinter import messagebox


def limpiar_pantalla():# esta funcion limpia la terminal en ejecucion.
    os.system('cls' if os.name == 'nt' else 'clear')


def pantalla_inicio_sesion():
    resultado_login = {'exitoso': False} 

    try:
        df_usuarios = pd.read_csv("usuarios.csv")
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo 'usuarios.csv'")
        return False

    def verificar_login():
        usuario_ingresado = entrada_usuario.get()
        contrasena_ingresada = entrada_contrasena.get()

        usuario_filtrado = df_usuarios[df_usuarios['USUARIO'] == usuario_ingresado]

        if not usuario_filtrado.empty:
            if usuario_filtrado.iloc[0]['CONTRASEÑA'] == contrasena_ingresada:
                messagebox.showinfo("Login exitoso", f"¡Bienvenido, {usuario_ingresado}!")
                resultado_login['exitoso'] = True
                ventana.destroy()
            else:
                messagebox.showerror("Error", "Contraseña incorrecta")
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def al_cerrar_ventana():
        if messagebox.askokcancel("Salir", "¿Desea cerrar la aplicación?"):
            ventana.destroy()

    ventana = tk.Tk()
    ventana.title("Inicio de Sesión")
    ventana.geometry("300x180")
    ventana.resizable(False, False)

    ventana.protocol("WM_DELETE_WINDOW", al_cerrar_ventana)

    tk.Label(ventana, text="Usuario:").pack(pady=5)
    entrada_usuario = tk.Entry(ventana)
    entrada_usuario.pack()

    tk.Label(ventana, text="Contraseña:").pack(pady=5)
    entrada_contrasena = tk.Entry(ventana, show="*")
    entrada_contrasena.pack()

    tk.Button(ventana, text="Iniciar sesión", command=verificar_login).pack(pady=15)

    ventana.mainloop()

    return resultado_login['exitoso']
                
                
def config_usuario(login): #Funcion que nos permite cambiar la contraseña de un usuario o crear uno nuevo si somos administradores ......
    
    df_usuarios = pd.read_csv("usuarios.csv")       #pasamos la base de datos de Usuario a un Dataframe    

    while True:
        try:
            print(Fore.LIGHTGREEN_EX+emoji.emojize('\n1️⃣  . Crear un nuevo usuario. '))
            print(Fore.LIGHTGREEN_EX+emoji.emojize('\n2️⃣  . Cambiar contraseña.'))
            print(Fore.LIGHTGREEN_EX+emoji.emojize('\n3️⃣  . Volver al menú principal. '))
            
           
            
            opcion_usuario = input(Fore.LIGHTGREEN_EX+emoji.emojize(f'\n#️⃣  Ingrese el numero de la opción que desee: '))
            
            limpiar_pantalla()
            
            if opcion_usuario == '1':
                
                usuario_admin = str(input('\n🔹 Ingrese su usuario: '))
                
                contraseña_admin = str(input('\n🔹 Ingrese la contraseña: '))
                
                acceso_correcto = ((df_usuarios['USUARIO'] == usuario_admin) &  (df_usuarios['CONTRASEÑA']== contraseña_admin)).any()
                
                
                if acceso_correcto and usuario_admin == 'Carlosmoya15':
                    
                    user_nuevo = str(input(Fore.LIGHTGREEN_EX+emoji.emojize('\n🔹 Ingrese nuevo usuario que quiere crear: ')))
                    contra_nuevo = str(input(Fore.LIGHTGREEN_EX+emoji.emojize('\n🔹 Ingrese la contraseña del nuevo usuario')))
                    
                    nuevo_usuario = {'USUARIO': user_nuevo, 'CONTRASEÑA': contra_nuevo}
                    
                    nuevo_df = pd.DataFrame([nuevo_usuario])

                    archivo_csv = 'usuarios.csv'

                    
                    if os.path.exists(archivo_csv):# Si el archivo ya existe, lo abrimos y agregamos
                        df_usuarios = pd.read_csv(archivo_csv)
                        df_usuarios = pd.concat([df_usuarios, nuevo_df], ignore_index=True)
                    else:
                        df_usuarios = nuevo_df

                    
                    df_usuarios.to_csv(archivo_csv, index=False)# Guardar CSV sin índice
                    
                    limpiar_pantalla()

                    print(Fore.LIGHTGREEN_EX+emoji.emojize('\n✅  Usuario guardado exitosamente.'))
                    
                  
                
            elif opcion_usuario == '2':
                
                usuario = str(input(Fore.LIGHTGREEN_EX+emoji.emojize('\n🔹Escriba el nombre de usuario: ')))
                contraseña = str(input(Fore.LIGHTGREEN_EX+emoji.emojize('\n🔹Escriba la contraseña: ')))
                
                
                
                if ((df_usuarios['USUARIO'] == usuario) & (df_usuarios['CONTRASEÑA'] == contraseña)).any():#Compara si los datos ingresados son iguales a los datos en el df.
                    
                    contraseña_nueva = input('Digite la nueva contraseña')
                    
                    df_usuarios.loc[df_usuarios['USUARIO']==usuario,'CONTRASEÑA'] = contraseña_nueva #cambia el valor de la contraseña en el dataframe
                    
                    df_usuarios.to_csv('usuarios.csv', index=False)#sobre escribe el df completo
                    
                    
                    
                    print(Fore.LIGHTGREEN_EX+emoji.emojize('\n✅Contraseña modificada exitosamente....')) 
            
            elif opcion_usuario == '3':
                break
                

            else:
                print(Fore.LIGHTGREEN_EX+emoji.emojize('❌ Usuario o contraseña no validos, Intentelo de nuevo '))     
                
        except ValueError:
                print(Fore.LIGHTGREEN_EX+emoji.emojize('❌Error: ingrese los datos correctamente.❌ '))
                continue


def consulta():  # Esta función permite consultar lo que hay en el archivo CSV donde se guardan los datos.
    while True:
        df_inventario = pd.read_csv('ferreteria.csv')  # Convierte el CSV en un DataFrame para poder trabajarlo.
        
        pd.set_option('display.max_rows', None)        # Mostrar todas las filas
        pd.set_option('display.max_columns', None)     # Mostrar todas las columnas
        pd.set_option('display.width', None)           # No limitar el ancho
        pd.set_option('display.max_colwidth', None)    # No truncar el texto de las columnas
        
        print(Fore.LIGHTGREEN_EX + emoji.emojize('\n📦 Inventario actual:\n'))
        print(Fore.WHITE + df_inventario.to_string(index=False))
        
        # Consultamos por un artículo específico que estemos buscando
        consulta_nombre = input(Fore.CYAN + emoji.emojize('\n🔍 Ingrese el nombre del artículo que desea consultar: ')).upper()
        
        if consulta_nombre in df_inventario['NOMBRE'].values:
            articulo = df_inventario[df_inventario['NOMBRE'] == consulta_nombre]
            print(Fore.LIGHTYELLOW_EX + emoji.emojize('\n✅ Artículo encontrado:\n'))
            print(Fore.WHITE + articulo.to_string(index=False))
        else:
            print(Fore.RED + emoji.emojize('\n❌ El artículo no está en el inventario.'))
        
        # Preguntamos si desea hacer otra consulta
        repetir = input(Fore.CYAN + emoji.emojize('\n🔁 ¿Desea consultar otro artículo? (S/N): ')).upper()
        if repetir == 'S':
            consulta()  # Llamada recursiva (podría mejorarse usando solo el bucle)
        elif repetir == 'N':
            print(Fore.GREEN + emoji.emojize('\n👋 Saliendo del módulo de consulta...'))
            break
        else:
            print(Fore.RED + emoji.emojize('\n⚠️ Opción no válida. Intente nuevamente.'))
            

def salida_inv():
    limpiar_pantalla()
    
    df_inventario = pd.read_csv('ferreteria.csv', encoding='utf-8')# convertimos el Csv del inventario en un DFrame de Pandas
    
    pd.set_option('display.max_rows', None)  # Para mostrar todas las filas
    pd.set_option('display.max_columns', None)  # Para mostrar todas las columnas
    pd.set_option('display.width', None)  # Para no limitar el ancho
    pd.set_option('display.max_colwidth', None)  # Para no truncar el texto de las columnas
    
    print(Fore.LIGHTRED_EX + df_inventario.to_string() + Style.RESET_ALL)
    
    while True: #inicio del Bucle
        
        init() 
        
        print(Fore.LIGHTGREEN_EX+emoji.emojize('\nPara Hacer una Salida del Inventario ingrese el numero 1: ') + Style.RESET_ALL)
        print(Fore.LIGHTGREEN_EX+emoji.emojize('Para Volver al Menú Principal ingrese el numero 2: ') + Style.RESET_ALL)
        
        accion = input((Fore.LIGHTGREEN_EX+emoji.emojize('\nQue desea hacer: ')))
        
        if accion == '1':
            try:
                nombre_art = input((Fore.LIGHTGREEN_EX+emoji.emojize('\nIngrese el nombre del Articulo: '))).upper()
                marca = input((Fore.LIGHTGREEN_EX+emoji.emojize('ingrese la Marca del fabricante: '))).upper()
                cantidad = int(input((Fore.LIGHTGREEN_EX+emoji.emojize('Digite la cantidad que deseea sacar del Sistema: ')+ Style.RESET_ALL)))
                
            except ValueError:
                print(Fore.LIGHTGREEN_EX+emoji.emojize('error: ingrese una opcion valida: ')+ Style.RESET_ALL)  
                continue
            
            # toma el nombre ingresado y en caso de estar  en el inventario nos 
            if nombre_art in df_inventario['NOMBRE'].values:
                df_inventario.loc[df_inventario['NOMBRE']==nombre_art,'CANTIDAD'] -= cantidad# resta la cantidad ingresada
                
            else:
                print('\nEl Articulo no se encuentra en sistema: ')
                
                # almacena directamente la nueva cantidad de los articulos
                df_inventario.to_csv('ferreteria.csv', index=False)
                print(df_inventario)

            print(Fore.LIGHTGREEN_EX+emoji.emojize('\n💾 Cambios guardados con exito.'))
            
            repetir = input('Desea hacer otra Salida? s/n? : ').upper() # damos la opcion de continuar o salir
            
            if repetir == 'S':
                print('\n---Salida de otro articulo---')
            
            elif repetir == 'N':
                print('Volviendo al menú principal')
                break
            else: 
                print('Ingrese una letra correcta, s/n: ')  
        
        elif accion == '2':
            break     
            
            
        print(Fore.LIGHTRED_EX + df_inventario.to_string() + Style.RESET_ALL)
         
       
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
            df_inventario.to_csv('ferreteria.csv', index=False) # guardamos la modificacion en el archivo csv
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
                                   

def guardar_ingreso(modificacion):
    if not modificacion:
        print('No hay ingresos que guardar en el CSV')
        return

    archivo_csv = 'ferreteria.csv'
    fieldnames = ['NOMBRE', 'MARCA', 'CANTIDAD', 'PRECIO']
    datos_existentes = []

    # Leer datos existentes si el archivo ya existe
    if os.path.exists(archivo_csv):
        with open(archivo_csv, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            datos_existentes = list(lector)
   
    nuevos_datos = modificacion

    # Crear un diccionario con claves compuestas (NOMBRE, MARCA) para acceso rápido
    datos_dict = {(item['NOMBRE'], item['MARCA']): item for item in datos_existentes}

    # actualiza o agrega los nuevos datos, esto soluciona la duplicacio
    for nuevo in nuevos_datos:
        clave = (nuevo['NOMBRE'], nuevo['MARCA'])
        if clave in datos_dict:
            # Actualizar los valores existentes
            datos_dict[clave]['CANTIDAD'] = nuevo['CANTIDAD']
            datos_dict[clave]['PRECIO'] = nuevo['PRECIO']
        else:
            # Agregar nuevo registro
            datos_dict[clave] = nuevo

    # Escribir todo nuevamente al archivo
    with open(archivo_csv, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=fieldnames)
        escritor.writeheader()
        escritor.writerows(datos_dict.values())

    modificacion.clear()
    print('Datos guardados exitosamente.')


def analizis_inv(): # pandas me permite ver algunos datos que pueden ser de relevancia para el usuario.
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
    
    
def exportar_inv():
    while True:
        descargar_inventario = input('''\n📦 Si desea descargar el inventario, digite \033[1;34m1\033[0m o presione ENTER para volver al menú principal: ''')

        if descargar_inventario == "1":
            try:
                # Leer archivo existente
                df = pd.read_csv("ferreteria.csv")
                
                # Ruta personalizada
                ruta = 'A:/Download'
                
                # Verifica si la carpeta existe
                if not os.path.exists(ruta):
                    print(f"\033[1;33m⚠️ La carpeta {ruta} no existe. Por favor, verifica la ruta.\033[0m")
                    return
                
                # Construir ruta completa del archivo
                ruta_archivo = os.path.join(ruta, "inventario.csv")
                df.to_csv(ruta_archivo, index=True, index_label="ID", sep=";", encoding="utf-8-sig")# el ; me ayudan a que exel me separe cada columna del inventario y no coloque todo en la columna A
                
                print(f"\033[1;32m✅ Archivo guardado correctamente en: {ruta_archivo}\033[0m")
                
            except FileNotFoundError:
                print("\033[1;31m❌ El archivo 'ferreteria.csv' no fue encontrado.\033[0m")
            except Exception as e:
                print(f"\033[1;31m❌ Ocurrió un error: {e}\033[0m")
        else:
            print("\033[1;36m🔙 Regresando al menú principal...\033[0m")
            break
    
        
def soporte_tecnico(): #con esta funcióm le doy una direccion para contactar a soporte tecnico.
    
    print(Fore.LIGHTYELLOW_EX+emoji.emojize("\n📧 Para contactar a Soporte tecnico envie un correo a la siguiente direccion. "))       
    
    print(Fore.LIGHTGREEN_EX+emoji.emojize("\nSoportemoyainvent@outlook.com")) 
    
    salir = input(Fore.LIGHTYELLOW_EX+emoji.emojize("\n🔙  Para voler al menú principal presione ENTER... ⌨ "))     
    return # hace que la funcion termine y regrese al menú principal...
    
    
def cerrar_sesion():
    respuesta = messagebox.askyesno("Cerrar sesión", "¿Desea cerrar sesión?")
    
    if respuesta:
        login_exitoso = pantalla_inicio_sesion()
        return login_exitoso  # True si el login fue exitoso, False si no
    else:
        print("Volviendo al menú principal...")
        return True  # Se queda en el menú