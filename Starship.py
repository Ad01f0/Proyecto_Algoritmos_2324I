#Clase de las naves
class Starship:
   def __init__(self, model, length, cargo_capacity,hyperdrive_rating, MGLT, url): 
    self.model= model
    self.length= length
    self.cargo_capacity= cargo_capacity
    self.hyperdrive_rating = hyperdrive_rating
    self.MGLT= MGLT
    self.url = url 