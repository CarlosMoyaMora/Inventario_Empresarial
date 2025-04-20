""" Este es mi proyecto final para el curso de fundamentos de Python en la UNCA
    Autor: Carlos Andrey Moya Mora
    Año: 2025
    Versón: 0.1
"""
import os






def menu_opciones():
    while True:
        print('____Bienvenido al menú del Sistema de Inventarios____')
        print('\n 1. Consultar Inventario: ')
        print('\n 2. Realizar una Salida del Inventario: ')
        print('\n 3. Realizar una entrada al Inventario: ')
        print('\n 4. Guardar los Cambios en el archivo CSV: ')
        print('\n 5. Analizar datos')
        print('\n 6. Ver graficos de compras y ventas')
        print('\n 7. Salir')
        
        opcion = input(f'\nIngrese el numero de la opcion que desee Realizar: ')
        
        if opcion == '1':
            print('Consulta de Inventario:')
        
        elif opcion == '2':
            print('Realizar una salida del Inventario')
        
        elif opcion == '3':
            print('Realizar una entrada al Inventario')
        
        elif opcion == '4':
            print('Guardar cambios en CSV') 
        
        elif opcion == '5':
            print('Analisis de datos del Inventario')
        
        elif opcion == '6':
            print('Graficos de compras y ventas')
            
        elif opcion == '7':
            print('Gracias por utilizar nuestro Sistema.')
            break
        
        else: 
            print('Opcion no Valida, Ingrese un Numero Valido')          
                    
        
        
        
        
        
        

### Aqui se va a Realizar la Ejecucion de el Codigo.

if __name__ == '__inventaio__':
    print('Bienvenido al sistema de Gestion de Ventas')


    menu_opciones()        