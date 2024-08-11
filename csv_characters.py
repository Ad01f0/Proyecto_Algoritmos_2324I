import pandas as pd

def getRowsFromCsv(file_path):
    df = pd.read_csv(file_path)
    return df.iterrows()

# Clase de importar personajes
class Characters:
    def __init__(self, id, nombre, origen):
        self.id=id 
        self.nombre=nombre
        self.origen=origen
        

def characters_from_csv(): 
    path_characters = 'CSV/characters.csv'
    rows = getRowsFromCsv(path_characters)
    
    characters = []
    for _ , row in rows:
            character = Characters(
                row['id'],
                row['name'],
                row ['homeworld']  
            )
            print(character.nombre)
            characters.append(character)
characters_from_csv()