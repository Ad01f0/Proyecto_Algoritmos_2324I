#Clase de los planetas 
class Planet:
   def __init__(self, name, orbital_period,rotation_period, population, climate, url): 
    self.name = name
    self.orbital_period= orbital_period
    self.rotation_period = rotation_period
    self.population = population
    self.climate = climate
    self.url = url 
    
   def show(self):
     print(f"Nombre: {self.name}\n Período de órbita.: {self.orbital_period}\nCantidad de habitantes: {self.population}\nTipo de clima:{self.climate}")