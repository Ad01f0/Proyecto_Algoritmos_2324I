import pandas as pd

def getRowsFromCsv(file_path):
    df = pd.read_csv(file_path)
    return df.iterrows()

# Clase de importar naves
class Starships:
    def __init__(self, id, nombre, cost_in_credits, length, max_atmosphering_speed, cargo_capacity, hyperdrive_rating, MGLT, starship_class):
        self.id=id 
        self.nombre=nombre
        self.cost_in_credits = cost_in_credits
        self.length=length
        self.max_atmosphering_speed= max_atmosphering_speed
        self.cargo_capacity=cargo_capacity
        self.hyperdrive_rating = hyperdrive_rating
        self.MGLT = MGLT
        self.starship_class= starship_class

def starships_from_csv(): 
    path_starships= 'CSV/starships.csv'
    rows = getRowsFromCsv(path_starships)
    
    starships = []
    for _ , row in rows:
        starship = Starships(
                row['id'],
                row['name'],
                row['cost_in_credits'],
                row['length'], 
                row['max_atmosphering_speed'], 
                row['cargo_capacity'],
                row['hyperdrive_rating'],
                row['MGLT'],
                row['starship_class'])
    
    starships.append(starship)
starships_from_csv()

            









