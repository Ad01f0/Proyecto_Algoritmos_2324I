#Clase de los planetas 
class Planet:
   def __init__(self, name, orbital_period,rotation_period, population, climate, url): 
    self.name = name
    self.orbital_period= orbital_period
    self.rotation_period = rotation_period
    self.population = population
    self.climate = climate
    self.url = url 
    
   def show(self, filmName, homeworldCharacters ):
      print(f"Nombre del planeta: {self.name}\nPeríodo de órbita: {self.orbital_period}\nPeríodo de rotación: {self.rotation_period}\nCantidad de habitantes: {self.population}\nTipo de clima:{self.climate}\nEpisodios en los que aparece el planeta: ")
      for name in filmName:
        print(name)
      print("Peronajes originarios del planeta: ")
      for name in homeworldCharacters:
        print(name)
