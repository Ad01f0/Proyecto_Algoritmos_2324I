from Mision import crear_misiones

class menu_misiones:

    while(True):
        menu = input('''
                        Ingrese una opción de las misiones:
                        1._ Construir misión
                        2._ Modificar misión
                        3._ Visualizar misión  
                        4._ Guardar misiones 
                        5._ Cargar misiones
                        6._ Salir                             
                        --> ''')
        if menu== '1':
            crear_misiones()
        if menu== '2':
            None
        if menu== '3':
            None
        if menu== '4':
            None
        if menu== '5':
            None
        if menu== '6':
            None
        else:print('Ingrese una opción valida')
