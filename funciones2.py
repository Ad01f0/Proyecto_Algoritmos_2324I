import requests as rq
import Film


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

        film = Film(title, )
        dbfilms.append(film)
        print(title)
    
cargar_info()