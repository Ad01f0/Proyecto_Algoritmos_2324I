#Clase de los personajes 
class Character:
   def __init__(self, name, homeworld, gender, url): 
    self.name= name
    self.homeworld= homeworld
    self.gender = gender
    self.url = url
    

   def show(self):
     print(f'''nombre del personaje: {self.name}
           planeta de origen: {self.homeworld}
           episodios en los que interviene:
           genero: {self.gender}
           especie:
           naves que utiliza:
           vehiculos que utiliza:
            ''')