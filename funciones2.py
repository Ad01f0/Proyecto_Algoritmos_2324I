import requests as rq
import Film
import Planets


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
    planets_API=cargar_SWAPIs("https://www.swapi.tech/api/planets?page=1&limit=2000")
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

        film = Film(title, )
        dbfilms.append(film)
        print(title)

    for general_planets in planets_API['result']:
        url = general_planets["url"]
        info_planets = rq.get(url).json()
        planets = info_planets["result"]["propierties"]["planets"]
        name = general_planets['properties']['name']
        orbital_period = general_planets['properties']['orbital_period']
        rotation_period = general_planets['properties']['rotation_period']
        population = general_planets['properties']['population']
        climate = general_planets['properties']['climate']
        

        planets = Planets( name,  orbital_period,rotation_period, population, climate) 
        dbplanets.append(planets)
        print(title)

cargar_info()