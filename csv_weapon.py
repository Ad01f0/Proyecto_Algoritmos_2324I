import pandas as pd

def getRowsFromCsv(file_path):   #Carga información del CSV de armas
    df = pd.read_csv(file_path)
    return df.iterrows()

class Weapon:
    def __init__(self, id, name, model,	manufacturer, cost_in_credits,	length,	type,	description,	films): 
        self.id = id
        self.name = name
        self.model = model
        self.manufacturer= manufacturer
        self.cost_in_credits = cost_in_credits
        self.length= length
        self.type = type
        self.description = description
        self.films= films

    def show(self):
        return (f'Nombre: {self.name}\n'
                f'Modelo: {self.model}\n'
                f'Manofacturador: {self.manufacturer}\n'
                f'Costo en creditos: {self.cost_in_credits}\n'
                f'Longitud: {self.length}\n'
                f'Tipo: {self.type}\n'
                f'Descripcion: {self.description}\n'
                f'Peliculas donde aparece: {self.films}\n')

def weapons_from_csv():    #Almacena la información del CSV de arma
    path_weapons= 'CSV/weapons.csv'
    rows = getRowsFromCsv(path_weapons)
    
    weapons = []
    for _ , row in rows:
        weapon = Weapon(
                row['id'],
                row['name'],
                row['model'],
                row['manufacturer'],
                row['cost_in_credits'],
                row['length'],
                row['type'],
                row['description'],
                row['films']
                )
        weapons.append(weapon)
    return weapons
weapons = weapons_from_csv()

 
