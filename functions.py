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


def pantalla_inicio_sesion(): #funcion que invoca la ventana para inicio de sesion
    resultado_login = {'exitoso': False} 

    try:
        df_usuarios = pd.read_csv("usuarios.csv")# dataframe de el CSv de usuarios
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo 'usuarios.csv'")
        return False

    def verificar_login(): #Funcion que verfica el login ingresado por el usuario. (Debe coincidir la contraseña con el usuario)
        usuario_ingresado = entrada_usuario.get()
        contrasena_ingresada = entrada_contrasena.get()

        usuario_filtrado = df_usuarios[df_usuarios['USUARIO'] == usuario_ingresado]# variable que almacena y comprueba que el usuario ingresado sea el mismo que se encuentra en el CSV

        if not usuario_filtrado.empty: # Esta condición lo que hace es verificar si se ingresó un valor, esto soluciona el echo de cerrar la ventana y que el codigo continue funcionando
            if usuario_filtrado.iloc[0]['CONTRASEÑA'] == contrasena_ingresada:
                messagebox.showinfo("Login exitoso", f"¡Bienvenido, {usuario_ingresado}!")
                resultado_login['exitoso'] = True
                ventana.destroy()
            else:
                messagebox.showerror("Error", "Contraseña incorrecta")
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def al_cerrar_ventana(): #esta función me da un mensaje cuando cierro la ventana con la X
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

    return resultado_login['exitoso']#Este return es el esperado por el codigo principal, en caso de obtener un false, el codigo no se ejecuta mas y se cierra el programa.
                
                
def config_usuario(login): #Funcion que nos permite cambiar la contraseña de un usuario o crear uno nuevo si somos administradores ......
    
    
    df_usuarios = pd.read_csv("usuarios.csv")       #pasamos la base de datos de Usuario a un Dataframe    

    while True:
        try:
            
            limpiar_pantalla()
            
            print(Fore.LIGHTGREEN_EX+emoji.emojize('\n1️⃣  . Crear un nuevo usuario. '))
            print(Fore.LIGHTGREEN_EX+emoji.emojize('\n2️⃣  . Cambiar contraseña.'))
            print(Fore.LIGHTGREEN_EX+emoji.emojize('\n3️⃣  . Volver al menú principal. '))
            
           
            
            opcion_usuario = input(Fore.LIGHTGREEN_EX+emoji.emojize(f'\n#️⃣  Ingrese el numero de la opción que desee: '))
            
            limpiar_pantalla()
            
            if opcion_usuario == '1':# si el usuario selecciona 1, la condiccion lo lleva a ingresar el usuario Admin
                
                usuario_admin = str(input('\n🔹 Ingrese el usuario de Administrador: '))
                
                contraseña_admin = str(input('\n🔹 Ingrese la contraseña de Administrador: '))
                
                #si el usuario y contraseña son de admin, se guardan en la variable acceso correcto
                acceso_correcto = ((df_usuarios['USUARIO'] == usuario_admin) &  (df_usuarios['CONTRASEÑA']== contraseña_admin)).any()
                
               
                #Esta condicion comprueba que el usuario almacenado sea el mismo que el registrado
                if acceso_correcto and usuario_admin == 'Carlosmoya15':
                    
                    user_nuevo = str(input(Fore.LIGHTGREEN_EX+emoji.emojize('\n🔹 Ingrese nuevo usuario que quiere crear: ')))
                    contra_nuevo = str(input(Fore.LIGHTGREEN_EX+emoji.emojize('\n🔹 Ingrese la contraseña del nuevo usuario: ')))
                    
                    nuevo_usuario = {'USUARIO': user_nuevo, 'CONTRASEÑA': contra_nuevo}
                    
                    nuevo_df = pd.DataFrame([nuevo_usuario])#crea un nuevo usuario y lo almacena en el df 

                    archivo_csv = 'usuarios.csv'#obtenemos el csv original

                    
                    if os.path.exists(archivo_csv):# Si el archivo ya existe, lo abre y agrega el nuevo usuario
                        df_usuarios = pd.read_csv(archivo_csv)
                        df_usuarios = pd.concat([df_usuarios, nuevo_df], ignore_index=True)
                    else:
                        df_usuarios = nuevo_df #de lo contrario redefinimos el dataframe usuarios

                    #aquí creariamos un nuevo CSV
                    df_usuarios.to_csv(archivo_csv, index=False)# Guardar CSV sin índice
                    
                    limpiar_pantalla()

                    print(Fore.LIGHTGREEN_EX+emoji.emojize('\n✅  Usuario guardado exitosamente.'))
                    
                  
                
            elif opcion_usuario == '2':#condicion if que ejecuta la segunda eleccion de usuario
                
                usuario = str(input(Fore.LIGHTGREEN_EX+emoji.emojize('\n🔹Escriba el nombre de usuario: ')))
                contraseña = str(input(Fore.LIGHTGREEN_EX+emoji.emojize('\n🔹Escriba la contraseña: ')))
                
                
                
                if ((df_usuarios['USUARIO'] == usuario) & (df_usuarios['CONTRASEÑA'] == contraseña)).any():#Compara si los datos ingresados son iguales a los datos en el df.
                    
                    contraseña_nueva = input('\n   Digite la nueva contraseña: ')#almacenamos la nueva contraseña del usuario
                    
                    df_usuarios.loc[df_usuarios['USUARIO']==usuario,'CONTRASEÑA'] = contraseña_nueva #cambia el valor de la contraseña en el dataframe
                    
                    df_usuarios.to_csv('usuarios.csv', index=False)#sobre escribe el df completo en el csv
                    
                    
                    
                    print(Fore.LIGHTGREEN_EX+emoji.emojize('\n✅Contraseña modificada exitosamente....')) 
            
            elif opcion_usuario == '3':#esta opcion me devuelve al menú
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
    
    df_inventario = pd.read_csv('ferreteria.csv', encoding='utf-8')  # Convertimos el CSV del inventario en un DataFrame de Pandas
    
    pd.set_option('display.max_rows', None)      # Para mostrar todas las filas
    pd.set_option('display.max_columns', None)   # Para mostrar todas las columnas
    pd.set_option('display.width', None)         # Para no limitar el ancho
    pd.set_option('display.max_colwidth', None)  # Para no truncar el texto de las columnas
    
    print(Fore.LIGHTRED_EX + df_inventario.to_string() + Style.RESET_ALL)
    
    while True:  # Inicio del bucle
        
        init()
        
        print(Fore.LIGHTGREEN_EX + emoji.emojize('\n📦 Para hacer una salida del inventario, ingrese el número 1: ') + Style.RESET_ALL)
        print(Fore.LIGHTGREEN_EX + emoji.emojize('🏠 Para volver al menú principal, ingrese el número 2: ') + Style.RESET_ALL)
        
        accion = input(Fore.LIGHTGREEN_EX + emoji.emojize('\n🔍 ¿Qué desea hacer?: ') + Style.RESET_ALL)
        
        if accion == '1':
            try:
                nombre_art = input(Fore.LIGHTGREEN_EX + emoji.emojize('\n🛠️ Ingrese el nombre del artículo: ') + Style.RESET_ALL).upper()
                marca = input(Fore.LIGHTGREEN_EX + emoji.emojize('🏷️ Ingrese la marca del fabricante: ') + Style.RESET_ALL).upper()
                cantidad = int(input(Fore.LIGHTGREEN_EX + emoji.emojize('➖ Digite la cantidad que desea sacar del sistema: ') + Style.RESET_ALL))
                
            except ValueError:
                print(Fore.LIGHTRED_EX + emoji.emojize('❌ Error: ingrese una opción válida.') + Style.RESET_ALL)  
                continue
            
            # Toma el nombre ingresado y en caso de estar en el inventario...
            if nombre_art in df_inventario['NOMBRE'].values:
                df_inventario.loc[df_inventario['NOMBRE'] == nombre_art, 'CANTIDAD'] -= cantidad  # Resta la cantidad ingresada
                
            else:
                print(Fore.LIGHTRED_EX + emoji.emojize('\n❗ El artículo no se encuentra en el sistema.') + Style.RESET_ALL)
            
            # Almacena directamente la nueva cantidad de los artículos
            df_inventario.to_csv('ferreteria.csv', index=False)
            print(Fore.LIGHTCYAN_EX + df_inventario.to_string() + Style.RESET_ALL)

            print(Fore.LIGHTGREEN_EX + emoji.emojize('\n💾 Cambios guardados con éxito.') + Style.RESET_ALL)
            
            repetir = input(Fore.LIGHTGREEN_EX + '🔁 ¿Desea hacer otra salida? (S/N): ' + Style.RESET_ALL).upper()
            
            if repetir == 'S':
                print(Fore.LIGHTYELLOW_EX + '\n---Salida de otro artículo---' + Style.RESET_ALL)
            
            elif repetir == 'N':
                print(Fore.LIGHTBLUE_EX + '↩️ Volviendo al menú principal...' + Style.RESET_ALL)
                break
            else: 
                print(Fore.LIGHTRED_EX + '⚠️ Ingrese una letra correcta (S/N).' + Style.RESET_ALL)
        
        elif accion == '2':
            print(Fore.LIGHTBLUE_EX + '↩️ Regresando al menú principal...' + Style.RESET_ALL)
            break     
        
        print(Fore.LIGHTRED_EX + df_inventario.to_string() + Style.RESET_ALL)

         
       
def entrada_inv(lista_articulos):  # Permite crear una entrada al inventario con lo que se desee ingresar.
    
    df_inventario = pd.read_csv('ferreteria.csv', encoding='utf-8')
    
    pd.set_option('display.max_rows', None)      # Para mostrar todas las filas
    pd.set_option('display.max_columns', None)   # Para mostrar todas las columnas
    pd.set_option('display.width', None)         # Para no limitar el ancho
    pd.set_option('display.max_colwidth', None)  # Para no truncar el texto de las columnas
    
    print(Fore.LIGHTCYAN_EX + df_inventario.to_string() + Style.RESET_ALL)
    
    while True:
        try:  # Solicita los datos que el usuario quiere ingresar al sistema
            nombre_art = input(Fore.LIGHTGREEN_EX + emoji.emojize('\n🛠️ Ingrese el nombre del artículo: ') + Style.RESET_ALL).upper()
            marca = input(Fore.LIGHTGREEN_EX + emoji.emojize('🏷️ Ingrese la marca del fabricante: ') + Style.RESET_ALL).upper()
            cantidad = int(input(Fore.LIGHTGREEN_EX + emoji.emojize('➕ Digite la cantidad que desea ingresar al sistema: ') + Style.RESET_ALL))
            precio = float(input(Fore.LIGHTGREEN_EX + emoji.emojize('💰 Ingrese el valor del artículo en colones: ') + Style.RESET_ALL))
        
        except ValueError:
            print(Fore.LIGHTRED_EX + emoji.emojize('❌ El valor no es correcto, por favor inténtelo nuevamente.') + Style.RESET_ALL)
            continue    

        # Verificamos si el artículo ya está en el inventario
        if nombre_art in df_inventario['NOMBRE'].values:
            df_inventario.loc[df_inventario['NOMBRE'] == nombre_art, 'CANTIDAD'] += cantidad  # Si existe, sumamos la cantidad
            df_inventario.to_csv('ferreteria.csv', index=False)  # Guardamos la modificación
            print(Fore.LIGHTCYAN_EX + df_inventario.to_string() + Style.RESET_ALL)
            print(Fore.LIGHTGREEN_EX + emoji.emojize('\n✅ Inventario actualizado.') + Style.RESET_ALL)
        
        else:
            # Si no existe, registramos un nuevo artículo (sin guardar en CSV, requiere confirmación en menú principal)
            modificacion = {'NOMBRE': nombre_art, 'MARCA': marca, 'CANTIDAD': cantidad, 'PRECIO': precio}
            lista_articulos.append(modificacion)
            print(Fore.LIGHTYELLOW_EX + emoji.emojize('\n🆕 Artículo nuevo registrado (no guardado en CSV):') + Style.RESET_ALL)
            print(Fore.LIGHTCYAN_EX + str(modificacion) + Style.RESET_ALL)
            print(Fore.LIGHTMAGENTA_EX + emoji.emojize('📌 No olvides guardar los datos en el menú principal.') + Style.RESET_ALL)

        # Opción de repetir
        repetir = input(Fore.LIGHTGREEN_EX + '🔁 ¿Desea hacer otro ingreso? (S/N): ' + Style.RESET_ALL).upper()
        
        if repetir == 'S':
            print(Fore.LIGHTYELLOW_EX + '\n---Ingresando otro artículo---' + Style.RESET_ALL)
        
        elif repetir == 'N':
            print(Fore.LIGHTBLUE_EX + '↩️ Volviendo al menú principal...' + Style.RESET_ALL)
            break
        else: 
            print(Fore.LIGHTRED_EX + '⚠️ Ingrese una letra correcta (S/N).' + Style.RESET_ALL)
     
                                   

def guardar_ingreso(modificacion): 
    if not modificacion:
        print(Fore.LIGHTRED_EX + emoji.emojize('⚠️ No hay ingresos que guardar en el CSV.') + Style.RESET_ALL)
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

    # Actualiza o agrega los nuevos datos, esto soluciona la duplicación
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
    print(Fore.LIGHTGREEN_EX + emoji.emojize('💾 Datos guardados exitosamente.') + Style.RESET_ALL)



def analisis_inv():  # Pandas permite ver algunos datos que pueden ser de relevancia para el usuario.
    while True:
        df_inv = pd.read_csv('ferreteria.csv', encoding='utf-8')

        print(Fore.LIGHTYELLOW_EX + emoji.emojize('\n📦 Artículos con mayor stock:') + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX, df_inv[df_inv['CANTIDAD'] == df_inv['CANTIDAD'].max()], Style.RESET_ALL)

        print(Fore.LIGHTYELLOW_EX + emoji.emojize('\n📉 Artículos con menor stock:') + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX, df_inv[df_inv['CANTIDAD'] == df_inv['CANTIDAD'].min()], Style.RESET_ALL)

        print(Fore.LIGHTYELLOW_EX + emoji.emojize('\n💸 Artículos de mayor valor:') + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX, df_inv[df_inv['PRECIO'] == df_inv['PRECIO'].max()], Style.RESET_ALL)

        print(Fore.LIGHTYELLOW_EX + emoji.emojize('\n💰 Artículos de menor valor:') + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX, df_inv[df_inv['PRECIO'] == df_inv['PRECIO'].min()], Style.RESET_ALL)

        # Datos adicionales de utilidad
        print(Fore.LIGHTYELLOW_EX + emoji.emojize('\n📊 Promedio de precios en inventario: ') + Style.RESET_ALL, end='')
        print(Fore.LIGHTMAGENTA_EX + f"₡{df_inv['PRECIO'].mean():,.2f}" + Style.RESET_ALL)

        print(Fore.LIGHTYELLOW_EX + emoji.emojize('\n📦 Total de artículos registrados: ') + Style.RESET_ALL, end='')
        print(Fore.LIGHTMAGENTA_EX + str(df_inv['NOMBRE'].nunique()) + Style.RESET_ALL)

        salir = input(Fore.LIGHTGREEN_EX + emoji.emojize('\n\n🔚 Para salir, digite 1: ') + Style.RESET_ALL)

        if salir == '1':
            break
        else:
            print(Fore.LIGHTRED_EX + emoji.emojize('⚠️ Por favor, digite un valor válido.') + Style.RESET_ALL)

    
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