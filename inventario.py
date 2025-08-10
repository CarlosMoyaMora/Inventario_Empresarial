""" Este es mi proyecto final para el curso de Desarrollo de Softwere con Python en la UNCA
    Autor: Carlos Andrey Moya Mora
    Año: 2025
    Versón: 0.06
"""

### Import necesarios para la ejecucion del programa
import os, emoji


from colorama import init,Fore,Back

# nos llama las Funciones de la pagina Functions para poder llamarlas al momento de ser requieridas.
from functions import *



    

def menu_opciones(): # Menu de opciones que le mostramos al usuario.
    
    while True:
        
        print(Fore.LIGHTGREEN_EX+emoji.emojize('\n _________________📚 Menú Principal 📚_________________')) #prints con Emojis para una visualizacion mas agradable
        print(Fore.LIGHTGREEN_EX+emoji.emojize('\n 1️⃣ . 📋  Consultar Inventario: '))
        print(Fore.LIGHTGREEN_EX+emoji.emojize('\n 2️⃣ . 📤  Realizar una Salida del Inventario: '))
        print(Fore.LIGHTGREEN_EX+emoji.emojize('\n 3️⃣ . 📥  Realizar una entrada al Inventario: '))
        print(Fore.LIGHTGREEN_EX+emoji.emojize('\n 4️⃣ . 💾  Guardar los Cambios en el archivo CSV: '))
        print(Fore.LIGHTGREEN_EX+emoji.emojize('\n 5️⃣ . 📊  Datos importantes sobre el inventario: '))
        print(Fore.LIGHTGREEN_EX+emoji.emojize('\n 6️⃣ . 🔐  Usuario y contraseña: '))
        print(Fore.LIGHTGREEN_EX+emoji.emojize('\n 7️⃣ . 🚀  Exportar Inventario a CSV: '))
        print(Fore.LIGHTGREEN_EX+emoji.emojize('\n 8️⃣ . ⚙️  Soporte Tecnico: '))
        print(Fore.LIGHTGREEN_EX+emoji.emojize('\n 9️⃣ . 🔚  Salir '))
        
        opcion = input(Fore.LIGHTGREEN_EX+emoji.emojize(f'\n #️⃣  Ingrese el numero de la opcion que desee Realizar: '))
        
        if opcion == '1':# Condicionales que nos llevaran a cada una de las funciones del menú
            limpiar_pantalla()
            print(Fore.RED+emoji.emojize('Consulta de Inventario:'))
            consulta()
        
        elif opcion == '2':
            limpiar_pantalla()
            print(Fore.RED+emoji.emojize('Realizar una salida del Inventario'))
            salida_inv()
        
        elif opcion == '3':
            limpiar_pantalla()
            print(Fore.RED+emoji.emojize('Realizar una entrada al Inventario'))
            entrada_inv(modificacion)
        
        elif opcion == '4':
            limpiar_pantalla()
            print(Fore.RED+emoji.emojize('\nGuardar cambios en CSV'))
            guardar_ingreso(modificacion)
            print(Fore.RED+emoji.emojize('\nArticulos guardados con exito.'))
            
        
        elif opcion == '5':
            limpiar_pantalla()
            print(Fore.LIGHTGREEN_EX+emoji.emojize('📊 Estos son algunos de los datos importantes del inventario'))        
            analizis_inv()
        
        elif opcion == '6':
            limpiar_pantalla()
            print(Fore.LIGHTGREEN_EX+emoji.emojize('🔧 Configuración de Usuario y contraseña.'))
            config_usuario(login)
            limpiar_pantalla()
        
        
        elif opcion == '7':
            limpiar_pantalla()
            print(Fore.RED+emoji.emojize('🚀 Exportar inventario.'))
            exportar_inv()
            
        
        elif opcion == '8':
            limpiar_pantalla()
            print(Fore.RED+emoji.emojize('🧑‍🔧 Soporte Tecnico.'))
            soporte_tecnico()
            
            
            
        elif opcion == '9':
            limpiar_pantalla()
            print(Fore.LIGHTYELLOW_EX+emoji.emojize('👋 Gracias por utilizar nuestro Sistema.'))
            break
        
        
        else:
            print(Fore.RED+emoji.emojize('🏴󠁢󠁳󠁥󠁸󠁿 Opcion no Valida, Ingrese un Numero Valido')) 
          
        
### Aqui se va a Realizar la Ejecucion de el Codigo.

if __name__ == '__main__':
    print('____Bienvenido al menú del Sistema de Inventarios____')
    
    login= [] #lista donde almaceno las modificaciones que realizo a los usuarios
    modificacion = [] #lista que almacena las modificaciones que le realizo al inventario
    #menu_login()
    menu_opciones()        