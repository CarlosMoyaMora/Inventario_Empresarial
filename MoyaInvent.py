""" 
Este es mi proyecto final para el curso de Desarrollo de Software con Python en la UNCA
Autor: Carlos Andrey Moya Mora
Año: 2025
Versión: 0.20
"""

### Imports necesarios para la ejecución del programa
import os, emoji
from colorama import init, Fore, Back

# Llamamos las funciones desde la página 'functions' para poder usarlas cuando sean requeridas.
from functions import *

def menu_opciones():  # Menú de opciones que le mostramos al usuario.
    
    if not pantalla_inicio_sesion():
        print("No se inició sesión. Saliendo del sistema.")
        return  # No permite que se ejecute el código si no se inicia sesión o se cierra la ventana
    
    while True:
        
        print(Fore.LIGHTGREEN_EX + emoji.emojize('\n _________________📚 Menú Principal 📚_________________'))
        print(Fore.LIGHTGREEN_EX + emoji.emojize('\n 1️⃣ . 📋  Consultar Inventario: '))
        print(Fore.LIGHTGREEN_EX + emoji.emojize('\n 2️⃣ . 📤  Realizar una salida del Inventario: '))
        print(Fore.LIGHTGREEN_EX + emoji.emojize('\n 3️⃣ . 📥  Realizar una entrada al Inventario: '))
        print(Fore.LIGHTGREEN_EX + emoji.emojize('\n 4️⃣ . 💾  Guardar los cambios en el archivo CSV: '))
        print(Fore.LIGHTGREEN_EX + emoji.emojize('\n 5️⃣ . 📊  Datos importantes sobre el inventario: '))
        print(Fore.LIGHTGREEN_EX + emoji.emojize('\n 6️⃣ . 🔐  Usuario y contraseña: '))
        print(Fore.LIGHTGREEN_EX + emoji.emojize('\n 7️⃣ . 🚀  Exportar Inventario a CSV: '))
        print(Fore.LIGHTGREEN_EX + emoji.emojize('\n 8️⃣ . ⚙️  Soporte Técnico: '))
        print(Fore.LIGHTGREEN_EX + emoji.emojize('\n 9️⃣ . 🏴  Cerrar Sesión: '))
        print(Fore.LIGHTGREEN_EX + emoji.emojize('\n 🔟 . 🔚  Salir del Programa. '))
        
        opcion = input(Fore.LIGHTGREEN_EX + emoji.emojize(f'\n #️⃣  Ingrese el número de la opción que desea realizar: '))
        
        if opcion == '1':
            limpiar_pantalla()
            print(Fore.RED + emoji.emojize('Consulta de Inventario:'))
            consulta()
        
        elif opcion == '2':
            limpiar_pantalla()
            print(Fore.RED + emoji.emojize('Realizar una salida del Inventario'))
            salida_inv()
        
        elif opcion == '3':
            limpiar_pantalla()
            print(Fore.RED + emoji.emojize('Realizar una entrada al Inventario'))
            entrada_inv(modificacion)
        
        elif opcion == '4':
            limpiar_pantalla()
            print(Fore.RED + emoji.emojize('\nGuardar cambios en CSV'))
            guardar_ingreso(modificacion)
            print(Fore.RED + emoji.emojize('\nArtículos guardados con éxito.'))
            
        elif opcion == '5':
            limpiar_pantalla()
            print(Fore.LIGHTGREEN_EX + emoji.emojize('📊 Estos son algunos de los datos importantes del inventario'))        
            analisis_inv()
        
        elif opcion == '6':
            limpiar_pantalla()
            print(Fore.LIGHTGREEN_EX + emoji.emojize('🔧 Configuración de usuario y contraseña.'))
            config_usuario(login)
            limpiar_pantalla()
        
        elif opcion == '7':
            limpiar_pantalla()
            print(Fore.RED + emoji.emojize('🚀 Exportar inventario.'))
            exportar_inv()
            
        elif opcion == '8':
            limpiar_pantalla()
            print(Fore.RED + emoji.emojize('🧑‍🔧 Soporte Técnico.'))
            soporte_tecnico()
            
        elif opcion == '9':
            limpiar_pantalla()
            if not cerrar_sesion():
                break  # Salir del bucle si no se volvió a iniciar sesión  
            
        elif opcion == '10':
            limpiar_pantalla()
            print(Fore.LIGHTYELLOW_EX + emoji.emojize('👋 Gracias por utilizar nuestro sistema.'))
            break
        
        else:
            print(Fore.RED + emoji.emojize('🏴 Opción no válida. Ingrese un número válido.')) 

        
### Aquí se va a realizar la ejecución del código.

if __name__ == '__main__':
    print('____Bienvenido al menú del Sistema de Inventarios____')
    
    login = []  # Lista donde almaceno las modificaciones que realizo a los usuarios
    modificacion = []  # Lista que almacena las modificaciones que realizo al inventario
    menu_opciones()
