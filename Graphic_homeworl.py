import matplotlib.pyplot as plt
import pandas as pd


def show_graphic1():

    try:
        data = pd.read_csv('CSV/characters.csv') #Carga datos de personajes desde el archivo CSV de personaje
    except: 
        print("No se ha podido cargar la data de los personajes")

    try: 
        homeworld_characters = data['homeworld'].value_counts() #Cacula el número de personajes nacidos por planeta

    except:
        print("Error al aplicar la función")
    
    try: 
        plt.figure(figsize=(12, 8))
        plt.barh(homeworld_characters.index, homeworld_characters.values, color='purple')
        plt.xlabel('Número de personajes')
        plt.ylabel('Planeta')
        plt.title('Número de personajes nacidos por cada planeta')
        plt.tight_layout()
        plt.show() # Muestra el gráfico

    except: 
        print("No se ha podido realizar el gráfico")
       


