# Clase de las peliculas

class Film:
  def __init__(self, title, episode_id, release_date, opening_crawl, director, species, characters, starships, vehicles):
    self.title = title
    self.episode_id = episode_id
    self.release_date = release_date
    self.opening_crawl = opening_crawl
    self.director = director
    self.species = species
    self.characters = characters
    self.starships = starships
    self.vehicles = vehicles


  def show(self):
    print(f"Titulo: {self.title}\nNúmero de episodio: {self.episode_id}\nFecha de lanzamiento: {self.release_date}\nNombre del director:{self.director}\nOpening crawl: {self.opening_crawl}")