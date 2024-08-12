import pandas as pd

def getRowsFromCsv(file_path): #Carga información del CSV de personaje
    df = pd.read_csv(file_path)
    return df.iterrows()

# Clase de importar personajes
class Characters:
    def __init__(self, id, name, homeworld, species, gender, height, weight, hair_color, eye_color, skin_color, year_born, year_died, description):
        self.id=id 
        self.name=name
        self.homeworld=homeworld
        self.species = species
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hair_color= hair_color
        self.eye_color = eye_color
        self.skin_color = skin_color
        self.year_born = year_born
        self.year_died = year_died
        self.description = description
    def show(self):
        return (f'Nombre: {self.name}\n'
                f'Origen: {self.homeworld}\n'
                f'Especie: {self.species}\n'
                f'Genero: {self.gender}\n'
                f'Altura: {self.height}\n'
                f'Peso: {self.weight}\n'
                f'Color de Pelo: {self.hair_color}\n'
                f'Color de ojos: {self.eye_color}\n'
                f'Color de piel: {self.skin_color}\n'
                f'Año de naciemiento: {self.year_born}\n'
                f'Año de muerte: {self.year_died}\n'
                f'Descripcion: {self.description}\n')

        

def characters_from_csv(): 
    path_characters = 'CSV/characters.csv'
    rows = getRowsFromCsv(path_characters)  #Almacena la información del CSV de personaje
    
    characters = []
    for _ , row in rows:
        character = Characters(
            row['id'],
            row['name'],
            row ['homeworld'],
            row['species'],
            row['gender'],
            row['height'],
            row['weight'],
            row['hair_color'],
            row['eye_color'],
            row['skin_color'],
            row['year_born'],
            row['year_died'],
            row['description'] 
            )
        characters.append(character)
    return characters
characters= characters_from_csv()

