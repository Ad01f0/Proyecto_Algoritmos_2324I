import requests as rq
from Planet import Planet
from Film import Film
from Species import Species
from Starship import Starship
from Character import Character
from Vehicle import Vehicle


def cargar_SWAPIs(link):
    try: 
        informacion = rq.get(link).json()
        return informacion
    except: 
        print("Error al cargar la data")

def cargar_info():
    dbfilms=[]
    dbplanets=[]
    dbcharacters=[]
    dbstarships=[]
    dbvehicles=[]
    dbspecies=[]

    films_API=cargar_SWAPIs("https://www.swapi.tech/api/films")
    planets_API=cargar_SWAPIs("https://www.swapi.tech/api/planets")
    characters_API=cargar_SWAPIs("https://www.swapi.tech/api/people")
    starships_API=cargar_SWAPIs("https://www.swapi.tech/api/starships")
    vehicles_API=cargar_SWAPIs("https://www.swapi.tech/api/vehicles")
    species_API=cargar_SWAPIs("https://www.swapi.tech/api/species")

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

        film = Film(title, episode_id, release_date, opening_crawl, director, species,characters,starships,vehicles)
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
            
            planets = Planet( name,  orbital_period,rotation_period, population, climate,url) 
            dbplanets.append(planets)
        except:
            print("Error al cargar la data")
       
    for general_species in species_API['results']:
        try:
            url = general_species["url"]
            info_species = rq.get(url).json()
            name = info_species['result']["properties"]["name"]
            average_height = info_species['result']['properties']['average_height']
            classification = info_species['result']['properties']['classification']
            language = info_species['result']['properties']['language']
            people = info_species['result']['properties']['people']
        
            species = Species(name, average_height, classification, language, people,url)
            dbspecies.append(species)
        except:
            print("Error al cargar la data")

    for general_characters in characters_API['results']:
        try:
            url = general_characters["url"]
            info_characters = rq.get(url).json()
            name = info_characters['result']["properties"]["name"]
            homeworld = info_characters['result']["properties"]['homeworld']
            gender = info_characters['result']['properties']['gender']

            characters = Character(name, homeworld, gender,url)
            dbcharacters.append(characters)
        except:
            print("Error al cargar la data")

    for general_vehicles in vehicles_API['results']:
        try:
            url = general_vehicles["url"]
            info_vehicles = rq.get(url).json()
            pilots_vehicles = info_vehicles['result']['properties']['pilots']
            
            vehicles = Vehicle(pilots_vehicles, url)
            dbvehicles.append(vehicles)
        except:
            print("Error al cargar la data")
        
    for general_starship in starships_API['results']:
        try:
            url = general_starship["url"]
            info_starships= rq.get(url).json()
            model = info_starships['result']['properties']['model']
            length = info_starships['result']['properties']['length']
            pilots = info_starships['result']['properties']['pilots']
            cargo_capacity = info_starships['result']['properties']['cargo_capacity']
            hyperdrive_rating = info_starships['result']['properties']['hyperdrive_rating']
            max_speed = info_starships['result']['properties']['max_atmosphering_speed']
            mglt = info_starships['result']['properties']['MGLT']
            cost = info_starships['result']['properties']['cost_in_credits']
            
            starships = Starship(model, pilots, length, cargo_capacity, hyperdrive_rating, cost, max_speed, mglt, url)
            dbstarships.append(starships)
        except:
            print("Error al cargar la data")
    
    return dbfilms, dbplanets, dbcharacters, dbstarships, dbvehicles, dbspecies    
    
