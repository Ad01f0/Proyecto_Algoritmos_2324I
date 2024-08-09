#Clase de las naves
class Starship:
   def __init__(self, model, pilots, length, cargo_capacity, hyperdrive_rating, cost, max_speed, MGLT, url): 
    self.model= model
    self.length= length
    self.pilots = pilots
    self.cargo_capacity= cargo_capacity
    self.hyperdrive_rating = hyperdrive_rating
    self.cost = cost
    self.max_speed = max_speed 
    self.MGLT= MGLT
    self.url = url