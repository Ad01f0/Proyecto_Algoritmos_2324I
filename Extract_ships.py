import csv

# Clase de importar naves
class Starships:
    def __init__(self, id, nombre, length, cargo_capacity, hyperdrive_rating, MGLT):
        self.id=id 
        self.nombre=nombre
        self.length=length
        self.cargo_capacity=cargo_capacity
        self.hyperdrive_rating = hyperdrive_rating
        self.MGLT = MGLT

    def importar_planetas(doc_de_origen):
        ships=[]
        with open(doc_de_origen, mode='r',encoding='utf-8') as archivo: 
            lector=csv.DictReader(archivo)
            for columna in lector:
                ships.append(Starships(columna['id'], columna['nombre'], columna['length'], columna['cargo_capacity'],columna['hyperdrive_rating'], columna['MGLT']))
                return ships
            









