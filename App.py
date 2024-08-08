from Usuario import Usuario
from funciones2 import cargar_SWAPIs
from funciones2 import cargar_info


class App:
        dbfilms, dbplanets, dbcharacters, dbstarships, dbvehicles, dbspecies = cargar_info()

        menu = input('''
                Ingrese una opcion del menú:
                1._ Lista de películas
                2._ Lista de especies de seres vivos
                3._ Lista de planetas
                4._ Buscar personaje
                5._ Gráficos y estadísticas
                6._ Crear misión
                7._ Modificar misión
                8._ Ver misión  
                9._ Guardar misión 
                10._ Cargar misión
                11._ Salir                             
                --> ''')
        print(dbfilms)
