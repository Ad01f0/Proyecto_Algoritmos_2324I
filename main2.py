import requests as rq
from Starship import Starship
from Character import Character
from Asignar_starships import asignar_starships
from characters_list_module import buscar_personaje

def cargar_SWAPIs(link):
    try: 
        informacion = rq.get(link).json()
        return informacion
    except: 
        print("Error al cargar la data")



dbstarships=[]
dbcharacters=[]
starships_API=cargar_SWAPIs("https://www.swapi.tech/api/starships?page=1&limit=100")
characters_API=cargar_SWAPIs("https://www.swapi.tech/api/people/14")

for general_starship in starships_API['results']:
   
            url = general_starship["url"]
            info_starships= rq.get(url).json()
            name = info_starships['result']['properties']['name']
            model = info_starships['result']['properties']['model']
            length = info_starships['result']['properties']['length']
            pilots = info_starships['result']['properties']['pilots']
            cargo_capacity = info_starships['result']['properties']['cargo_capacity']
            hyperdrive_rating = info_starships['result']['properties']['hyperdrive_rating']
            max_speed = info_starships['result']['properties']['max_atmosphering_speed']
            mglt = info_starships['result']['properties']['MGLT']
            cost = info_starships['result']['properties']['cost_in_credits']
            
            starships = Starship(model, pilots, name, length, cargo_capacity, hyperdrive_rating, cost, max_speed, mglt, url)
            dbstarships.append(starships)
  

for general_characters in characters_API['result']:

            url = general_characters["url"]
            info_characters = rq.get(url).json()
            name = info_characters["properties"]["name"]
            homeworld = info_characters["properties"]['homeworld']
            gender = info_characters['properties']['gender']
            species = "humano"
            starships = asignar_starships(dbstarships, url)

            characters = Character(name, homeworld, gender, species, starships, url)
            dbcharacters.append(characters)


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
                        
                        pass
                elif menu == '2':
                        
                        pass
                elif menu == '3':
                        
                        pass
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