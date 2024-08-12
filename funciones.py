import requests as rq
from Planet import Planet
from Film import Film
from Species import Species
from Starship import Starship
from Character import Character
from Vehicle import Vehicle
from Asignar_species import asignar_species
from Asignar_starships import asignar_starships
from Asignar_vehiculos import asignar_vehiculos
from Asignar_films import asignar_films
from Asingar_planeta import asignar_planeta

def cargar_SWAPIs(link): #Carga los datos desde el enlace de la API y devuelve la información en formato JSON
    try:  
        informacion = rq.get(link).json()
        return informacion
    except: 
        print("Error al cargar la data para SWAPIs")

def cargar_info():
    dbfilms=[]
    dbplanets=[]
    dbcharacters=[]
    dbstarships=[]
    dbvehicles=[]
    dbspecies=[]
   

    films_API=cargar_SWAPIs("https://www.swapi.tech/api/films?page=1&limit=100")
    planets_API=cargar_SWAPIs("https://www.swapi.tech/api/planets?page=1&limit=100")
    characters_API=cargar_SWAPIs("https://www.swapi.tech/api/people?page=1&limit=100")
    starships_API=cargar_SWAPIs("https://www.swapi.tech/api/starships?page=1&limit=100")
    vehicles_API=cargar_SWAPIs("https://www.swapi.tech/api/vehicles?page=1&limit=100")
    species_API=cargar_SWAPIs("https://www.swapi.tech/api/species?page=1&limit=100")

    for general_films in films_API['result']:
        title=general_films['properties']['title']
        episode_id=general_films['properties']['episode_id']
        release_date=general_films['properties']['release_date']
        opening_crawl=general_films['properties']['opening_crawl']      
        director=general_films['properties']['director']
        species=general_films['properties']['species']
        characters=general_films['properties']['characters']
        starships=general_films['properties']['starships']
        vehicles=general_films['properties']['vehicles']
        planets=general_films['properties']['planets']

        film = Film(title, episode_id, release_date, opening_crawl, director, species,characters,starships,vehicles, planets)
        dbfilms.append(film)

    for general_planets in planets_API['results']:
        url = general_planets["url"]
        try:
            info_planets = rq.get(url).json()
            name = info_planets['result']["properties"]['name']
            orbital_period = info_planets['result']["properties"]['orbital_period']
            rotation_period = info_planets['result']['properties']['rotation_period']
            population = info_planets['result']['properties']['population']
            climate = info_planets['result']['properties']['climate']
            
            planets = Planet(name,  orbital_period,rotation_period, population, climate,url) 
            dbplanets.append(planets)
        except:
            print("Error al cargar la data para planets")
       
    for general_species in species_API['results']:
        url = general_species["url"]
        try:
            info_species = rq.get(url).json()
            name = info_species['result']["properties"]["name"]
            homeworld = info_species['result']["properties"]["homeworld"]
            average_height = info_species['result']['properties']['average_height']
            classification = info_species['result']['properties']['classification']
            language = info_species['result']['properties']['language']
            people = info_species['result']['properties']['people']
            
            specie = Species(name, average_height, homeworld, classification, language, people, url)
            dbspecies.append(specie)
        except:
            print("Error al cargar la data para species")
           

    for general_starship in starships_API['results']:
        try:
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
        except:
            print("Error al cargar la data para starships")
           

    for general_vehicles in vehicles_API['results']:
        try:
            url = general_vehicles["url"]
            info_vehicles = rq.get(url).json()
            name = info_vehicles['result']['properties']['name']
            pilots = info_vehicles['result']['properties']['pilots']
            
            vehicles = Vehicle(name, pilots, url)
            dbvehicles.append(vehicles)
        except:
            print("Error al cargar la data para vehicles")
            

    for general_characters in characters_API['results']:
        try:
            url = general_characters["url"]
            info_characters = rq.get(url).json()
            name = info_characters['result']["properties"]["name"]
            gender = info_characters['result']['properties']['gender']
            homeworld = asignar_planeta(dbplanets, info_characters['result']["properties"]['homeworld'])
            species = asignar_species(dbspecies, url)
            starships = asignar_starships(dbstarships, url)
            vehicles = asignar_vehiculos(dbvehicles, url)
            films = asignar_films(dbfilms, url)

            characters = Character(name, homeworld, gender, species, starships, vehicles, films, url)
            dbcharacters.append(characters)
        except:
            print("Error al cargar la data para characters")
            


    return dbfilms, dbplanets, dbcharacters, dbstarships, dbvehicles, dbspecies


    
    
