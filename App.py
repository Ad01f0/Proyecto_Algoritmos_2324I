from funciones import cargar_info
from movies_list_module import show_movie_list
from planets_list_module import show_planets_list
from species_list_module import show_species_list
from characters_list_module import buscar_personaje

class App:

        dbfilms, dbplanets, dbcharacters, dbstarships, dbvehicles, dbspecies = cargar_info()
        
        while(True):
                menu = input('''
                        Ingrese una opcion del menú:
                        1._ Lista de películas
                        2._ Lista de especies de seres vivos
                        3._ Lista de planetas
                        4._ Buscar personaje
                        5._ Gráfico de cantidad de personajes nacidos en cada planeta
                        6._ Gráficos de características de naves
                        7._ Estadísticas sobre naves
                        8._ Construir misión
                        9._ Modificar misión
                        10._ Visualizar misión  
                        11._ Guardar misión 
                        12._ Cargar misión
                        13._ Salir                             
                        --> ''')
                
                if menu == '1':
                        
                        show_movie_list(dbfilms)
                elif menu == '2':
                        
                        show_species_list(dbspecies, dbplanets, dbfilms, dbcharacters)
                elif menu == '3':
                        
                        show_planets_list(dbplanets, dbfilms, dbcharacters)
                elif menu == '4':

                        buscar_personaje(dbcharacters)
                elif menu == '5':
                        
                        None
                elif menu == '6':
                        None
                elif menu == '7':
                        None
                elif menu == '8':
                        None
                elif menu == '9':
                        None
                elif menu == '10':
                        None  
                elif menu == '11':
                        None      
                elif menu == '12':
                        None       
                elif menu == '13':
                        break               