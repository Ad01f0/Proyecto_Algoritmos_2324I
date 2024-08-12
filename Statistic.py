import pandas as pd
import matplotlib.pyplot as plt
from csv_ships import starships  

def show_statistics():
    starship_classes = ['Speeder', 'Landspeeder', 'Starfighter', 'Airspeeder', 'Interceptor', 'Bomber', 'Gunship', 
                        'Auxiliary starfighter', 'Sloop', 'Assault starfighter', 'Assault ship', 'Transport', 'Yacht',   #Lista de clases de naves
                        'Light freighter', 'Haulcraft', 'Medium transport', 'Corvette', 'Dreadnought', 'Capital ship',  
                        'Battleship', 'Heavy cruiser', 'Star Dreadnought']

    hyperdrive_ratings = {}
    mglt_speeds = {}
    max_atmosphering_speeds = {}
    costs_in_credits = {}

    for starship_class in starship_classes:
        hyperdrive_ratings[starship_class] = []
        mglt_speeds[starship_class] = []
        max_atmosphering_speeds[starship_class] = []
        costs_in_credits[starship_class] = []

        for ship in starships:
            if getattr(ship, 'starship_class', None) == starship_class:
                hyperdrive_ratings[starship_class].append(getattr(ship, 'hyperdrive_rating', None))
                mglt_speeds[starship_class].append(getattr(ship, 'MGLT', None))
                max_atmosphering_speeds[starship_class].append(getattr(ship, 'max_atmosphering_speed', None))
                costs_in_credits[starship_class].append(getattr(ship, 'cost_in_credits', None))

    statistics = [] #Lista para las estadísticas

    for starship_class in starship_classes:
        class_stats = {
            'Class': starship_class,
            'Hyperdrive Rating Mean': pd.Series(hyperdrive_ratings[starship_class]).astype(float).mean(),
            'Hyperdrive Rating Mode': pd.Series(hyperdrive_ratings[starship_class]).astype(float).mode().iloc[0] if len(pd.Series(hyperdrive_ratings[starship_class]).astype(float).mode()) > 0 else None,
            'Hyperdrive Rating Min': pd.Series(hyperdrive_ratings[starship_class]).astype(float).min(),
            'Hyperdrive Rating Max': pd.Series(hyperdrive_ratings[starship_class]).astype(float).max(),
            'MGLT Mean': pd.Series(mglt_speeds[starship_class]).astype(float).mean(),
            'MGLT Mode': pd.Series(mglt_speeds[starship_class]).astype(float).mode().iloc[0] if len(pd.Series(mglt_speeds[starship_class]).astype(float).mode()) > 0 else None,
            'MGLT Min': pd.Series(mglt_speeds[starship_class]).astype(float).min(),
            'MGLT Max': pd.Series(mglt_speeds[starship_class]).astype(float).max(),
            'Max Atmosphering Speed Mean': pd.Series(max_atmosphering_speeds[starship_class]).astype(float).mean(),
            'Max Atmosphering Speed Mode': pd.Series(max_atmosphering_speeds[starship_class]).astype(float).mode().iloc[0] if len(pd.Series(max_atmosphering_speeds[starship_class]).astype(float).mode()) > 0 else None,
            'Max Atmosphering Speed Min': pd.Series(max_atmosphering_speeds[starship_class]).astype(float).min(),
            'Max Atmosphering Speed Max': pd.Series(max_atmosphering_speeds[starship_class]).astype(float).max(),
            'Cost in Credits Mean': pd.Series(costs_in_credits[starship_class]).astype(float).mean(),
            'Cost in Credits Mode': pd.Series(costs_in_credits[starship_class]).astype(float).mode().iloc[0] if len(pd.Series(costs_in_credits[starship_class]).astype(float).mode()) > 0 else None,
            'Cost in Credits Min': pd.Series(costs_in_credits[starship_class]).astype(float).min(),
            'Cost in Credits Max': pd.Series(costs_in_credits[starship_class]).astype(float).max(),
        }
        statistics.append(class_stats)

    statistics_data = pd.DataFrame(statistics)
    statistics_data = statistics_data.round(2)

    statistics_data.rename(columns={
        'Class': 'Clase de Nave',
        'Hyperdrive Rating Mean': 'Media CI',
        'Hyperdrive Rating Mode': 'Moda CI',
        'Hyperdrive Rating Min': 'Mínimo CI',
        'Hyperdrive Rating Max': 'Máximo CI',
        'MGLT Mean': 'Media MGLT',
        'MGLT Mode': 'Moda MGLT',
        'MGLT Min': 'Mínimo MGLT',
        'MGLT Max': 'Máximo MGLT',
        'Max Atmosphering Speed Mean': 'Media V Max',
        'Max Atmosphering Speed Mode': 'Moda V Max',
        'Max Atmosphering Speed Min': 'Mínima V Max',
        'Max Atmosphering Speed Max': 'Máxima V Max',
        'Cost in Credits Mean': 'Media Costo',
        'Cost in Credits Mode': 'Moda Costo',
        'Cost in Credits Min': 'Mínimo Costo',
        'Cost in Credits Max': 'Máximo Costo'
    }, inplace=True)

    fig, ax = plt.subplots(figsize=(14, 12))
    ax.axis('off')
    ax.axis('tight')

    table = ax.table(cellText=statistics_data.values, colLabels=statistics_data.columns, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(6)
    table.scale(1, 1.25)

    plt.title("Estadísticas de Clases de Naves", fontsize=20)
    plt.show()

