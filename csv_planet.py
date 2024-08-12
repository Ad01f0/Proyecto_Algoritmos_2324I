import pandas as pd

def getRowsFromCsv(file_path):  #Carga información del CSV de planeta
    df = pd.read_csv(file_path)
    return df.iterrows()
class Planet:
  
   def __init__(self, id, name): 
    self.id = id
    self.name = name

def planets_from_csv(): 
    path_planets= 'CSV/planets.csv'      #Almacena la información del CSV de planeta
    rows = getRowsFromCsv(path_planets)
    
    planets = []
    for _ , row in rows:
        planet = Planet(
                row['id'],
                row['name'],  
            )
        planets.append(planet)
    return planets

planets = planets_from_csv()




