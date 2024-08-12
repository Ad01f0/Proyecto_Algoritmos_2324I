from funciones import cargar_info
from movies_list_module import show_movie_list
from planets_list_module import show_planets_list
from species_list_module import show_species_list
from characters_list_module import buscar_personaje
from Mision import misiones
from Graphic_starship import graficos_naves
from Graphic_homeworl import show_graphic1
from Statistic import show_statistics
class App: #Clase principal 

        def __init__(self) -> None: 
                 self.dbfilms, self.dbplanets, self.dbcharacters, self.dbstarships, self.dbvehicles, self.dbspecies = cargar_info() #Función para cargar la información  
        
        
        def start(self): #Muestra menú interactivo
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
                                8._ Misiones
                                9._ Salir                             
                                --> ''')
                        
                        if menu == '1':
                                show_movie_list(self.dbfilms)
                        elif menu == '2':
                                
                                show_species_list(self.dbspecies, self.dbplanets, self.dbfilms, self.dbcharacters)
                        elif menu == '3':
                                
                                show_planets_list(self.dbplanets, self.dbfilms, self.dbcharacters)
                        elif menu == '4':
                                buscar_personaje(self.dbcharacters)
                        elif menu == '5':
                                show_graphic1()
                        elif menu == '6':
                                graficos_naves()
                        elif menu == '7':
                                show_statistics()
                        elif menu == '8':
                                misiones()
                        elif menu == '9':
                                break       
                        else:
                                print("Opción no válida. Por favor, intente de nuevo.") # Verificación para entradas no válidas en el menú