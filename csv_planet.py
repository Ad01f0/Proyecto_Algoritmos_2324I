import csv 
class Planet:
   def __init__(self, id, name, residents): 
    self.id = id
    self.name = name
    self.residents = residents
   

   ruta = "C:\\Users\\gabyp\\Documents\\proyecto_algoritmos\\starwars\\planets.csv"

   def planets_from_csv(ruta): 
    
    planets = []
    with open(ruta, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            planet = Planet(
                row['id'],
                row['name'],
                row['residents'],  
            )
            planets.append(planet)
    return planets
   
   def select_planet(planets):
    try:
        opcion = int(input("Seleccione un planeta: "))
        eleccion_planeta = planets[opcion - 1]
        print(f'Has seleccionado el planeta {eleccion_planeta.name}.')
        return eleccion_planeta
    except:
        print("Caracter inválido. Inténtalo nuevamente.")

    def show_planets (planets): 
       for i, planet in enumerate (planets,1):
          print("Seleccione un planeta")
          print(f'{i}.{planets.name}')
    




