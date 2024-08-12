
#Clase de los personajes 
class Character:
   def __init__(self, name, homeworld, gender, specie, starship, vehicle, films, url): 
    self.name= name
    self.homeworld= homeworld
    self.gender = gender
    self.specie = specie
    self.starship = starship
    self.vehicle = vehicle
    self.films = films
    self.url = url
    

   def show(self):
     print(f'''
           ------------------------------------------
           nombre del personaje: {self.name}
           planeta de origen: {self.homeworld}
           episodios en los que interviene: {self.films}
           genero: {self.gender}
           especie: {self.specie}
           naves que utiliza: {self.starship}
           vehiculos que utiliza: {self.vehicle}
           -------------------------------------------
            ''')