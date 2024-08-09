from Usuario import Usuario
from funciones import cargar_info
from movies_list_module import show_movie_list
from planets_list_module import show_planets_list

class App:
        dbfilms, dbplanets, dbcharacters, dbstarships, dbvehicles, dbspecies = cargar_info()
        while(True):
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
                
                if menu == '1':
                        show_movie_list(dbfilms)
                elif menu == '2':
                        show_planets_list(dbplanets)
                        
                elif menu == '11':
                        break