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
    planets_API=cargar_SWAPIs("https://www.swapi.tech/api/planets?page=1&limit=150")
    characters_API=cargar_SWAPIs("https://www.swapi.tech/api/people?page=0&limit=150%22")
    starships_API=cargar_SWAPIs("https://www.swapi.tech/api/starships?page=1&limit=150")
    vehicles_API=cargar_SWAPIs("https://www.swapi.tech/api/vehicles?page=1&limit=150")
    species_API=cargar_SWAPIs("https://www.swapi.tech/api/species?page=1&limit=150")

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
        info_planets = rq.get(url).json()
        name = info_planets['result']["properties"]['name']
        orbital_period = info_planets['result']["properties"]['orbital_period']
        rotation_period = info_planets['result']['properties']['rotation_period']
        population = info_planets['result']['properties']['population']
        climate = info_planets['result']['properties']['climate']
        
        planets = Planet( name,  orbital_period,rotation_period, population, climate,url) 
        dbplanets.append(planets)

       
    for general_species in species_API['results']:
        url = general_species["url"]
        info_species = rq.get(url).json()
        name = info_species['result']["properties"]["name"]
        average_height = info_species['result']['properties']['average_height']
        classification = info_species['result']['properties']['classification']
        language = info_species['result']['properties']['language']
        people = info_species['result']['properties']['people']
       
        species = Species(name, average_height, classification, language, people,url)
        dbspecies.append(species)

    for general_characters in characters_API['results']:
        url = general_characters["url"]
        info_characters = rq.get(url).json()
        name = info_characters['result']["properties"]["name"]
        homeworld = info_characters['result']["properties"]['homeworld']
        gender = info_characters['result']['properties']['gender']

        characters = Character(name, homeworld, gender,url)
        dbcharacters.append(characters)

    for general_vehicles in vehicles_API['results']:
        url = general_vehicles["url"]
        info_vehicles = rq.get(url).json()
        pilots_vehicles = info_vehicles['result']['properties']['pilots']
        
        vehicles = Vehicle(pilots_vehicles, url)
        dbvehicles.append(vehicles)

    for general_starship in starships_API['results']:
        url = general_starship["url"]
        info_starships= rq.get(url).json()
        pilots_starchips = info_starships['result']['properties']['pilots']
        cargo_capacity = info_starships['result']['properties']['cargo_capacity']
        hyperdrive_rating = info_starships['result']['properties']['hyperdrive_rating']
        MGLT = info_starships['result']['properties']['MGLT']


        
        starships = Starship(pilots_starchips, cargo_capacity,hyperdrive_rating, MGLT, url)
        dbstarships.append(starships)
