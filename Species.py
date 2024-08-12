class Species:
   def __init__(self, name, average_height, homeworld, classification, language, people, url): 
    self.name= name
    self.average_height = average_height
    self.homeworld = homeworld
    self.classification = classification
    self.language = language
    self.people = people
    self.url = url
    
   def show(self, peopleNames, homeworldName, episodeNames):
      print(f"Nombre de la especie: {self.name}\nAltura: {self.average_height}\nClasificación: {self.classification}\nPlaneta de origen: {homeworldName}\nLenguaje: {self.language}\nPersonajes que pertenecen a la especie:")
      for name in peopleNames:
        print(name)
      print("Episodios en los que aparece la especie: ")
      for name in episodeNames:
        print(name)

#Muestra detalles de la especie 