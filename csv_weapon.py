import pandas as pd

def getRowsFromCsv(file_path):
    df = pd.read_csv(file_path)
    return df.iterrows()

class Weapon:
   def __init__(self, id, name): 
    self.id = id
    self.name = name

def weapons_from_csv(): 
    path_weapons= 'CSV/weapons.csv'
    rows = getRowsFromCsv(path_weapons)
    
    weapons = []
    for _ , row in rows:
        weapon = Weapon(
                row['id'],
                row['name']
                )
    weapons.append(weapon)
weapons_from_csv()

 
