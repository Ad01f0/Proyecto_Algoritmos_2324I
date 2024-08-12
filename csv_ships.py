import pandas as pd

def getRowsFromCsv(file_path):
    df = pd.read_csv(file_path)
    return df.iterrows()

# Clase de importar naves
class Starships:
    def __init__(self, id, name,model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity,consumables, hyperdrive_rating, MGLT, starship_class, pilots, films):
        self.id=id 
        self.name=name
        self.model = model 
        self.manufacturer= manufacturer
        self.cost_in_credits = cost_in_credits
        self.length=length
        self.max_atmosphering_speed= max_atmosphering_speed
        self.crew= crew
        self.passengers= passengers
        self.cargo_capacity=cargo_capacity
        self.consumables= consumables
        self.hyperdrive_rating = hyperdrive_rating
        self.MGLT = MGLT
        self.starship_class= starship_class
        self.pilots= pilots
        self.films= films

    def show(self):
        return (f'Nombre: {self.name}\n'
                f'Modelo: {self.model}\n'
                f'Manofacturador: {self.manufacturer}\n'
                f'Costo en creditos: {self.cost_in_credits}\n'
                f'Longitud: {self.length}\n'
                f'Velocidad máxima en atmósfera: {self.max_atmosphering_speed}\n'
                f'Tripulacion: {self.crew}\n'
                f'Pasajeros: {self.passengers}\n'
                f'Capacidad de carga: {self.cargo_capacity}\n'
                f'Consumibles: {self.consumables}\n'
                f'Clasificación de hiperimpulsor: {self.hyperdrive_rating}\n'
                f'MGLT(Modern Galactic Light Time): {self.MGLT}\n'
                f'Clase: {self.starship_class}\n'
                f'Pilotos: {self.pilots}\n'
                f'Peliculas donde aparece: {self.films}\n')
        

def starships_from_csv(): 
    path_starships= 'CSV/starships.csv'
    rows = getRowsFromCsv(path_starships)
    
    starships = []
    for _ , row in rows:
        starship = Starships(
                row['id'],
                row['name'],
                row['model'],
                row['manufacturer'],
                row['cost_in_credits'],
                row['length'], 
                row['max_atmosphering_speed'], 
                row['crew'],
                row['passengers'],
                row['cargo_capacity'],
                row['consumables'],
                row['hyperdrive_rating'],
                row['MGLT'],
                row['starship_class'],
                row['pilots'],
                row['films']
                )
        starships.append(starship)

    return starships
starchips = starships_from_csv()



            









