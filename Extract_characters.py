import csv

# Clase de importar personajes
class Characters:
    def __init__(self, id, nombre):
        self.id=id 
        self.nombre=nombre
        

    def importar_personajes(doc_de_origen):
        people=[]
        with open(doc_de_origen, mode='r',encoding='utf-8') as archivo: 
            lector=csv.DictReader(archivo)
            for columna in lector:
                people.append(Characters(columna['id'], columna['nombre'], columna['length'], columna['cargo_capacity'],columna['hyperdrive_rating'], columna['MGLT']))
                return people