import pandas as pd

def getRowsFromCsv(file_path):
    df = pd.read_csv(file_path)
    return df.iterrows()
class Planet:
  
   def __init__(self, id, name): 
    self.id = id
    self.name = name

def planets_from_csv(): 
    path_planets= 'CSV/planets.csv'
    rows = getRowsFromCsv(path_planets)
    
    planets = []
    for _ , row in rows:
        planet = Planet(
                row['id'],
                row['name'],  
            )
        planets.append(planet)   

planets_from_csv()






