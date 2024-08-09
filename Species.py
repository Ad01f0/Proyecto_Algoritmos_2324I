class Species:
   def __init__(self, name, average_height, classification, language, people,url): 
    self.name= name
    self.average_height = average_height
    self.classification = classification
    self.language = language
    self.people = people
    self.url = url
    
   def show(self):
      print(f"Nombre: {self.name}\nAltura: {self.average_height}\nClasificación: {self.classification}\nLenguaje:{self.lenguage}\nPoblación: {self.people}")
