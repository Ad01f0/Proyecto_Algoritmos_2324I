import pandas as pd
import matplotlib.pyplot as plt

#Estas funciones cargan el CVS de naves para obtener la información necesaria para generar y mostrar los gráficos correspondientes. 

def show_graphic2():
    try:
        data = pd.read_csv('CSV/starships.csv') 
    except: 
        print("No se ha podido cargar la data de las naves")
    try: 
        
        plt.figure(figsize=(12, 10))
        plt.barh(data['name'], data['length'], color='pink')
        plt.xlabel('Longitud de la nave')
        plt.ylabel('Nombre de la nave')
        plt.title('Comparación de longitud de las naves')
        plt.xticks((range(0,20000, 1000)))
        plt.tight_layout()
        plt.show() 
        

    except:
        print("Error al aplicar la función")
        return(graficos_naves)

    

def show_graphic3():
    try:
        data = pd.read_csv('CSV/starships.csv')  
    except: 
        print("No se ha podido cargar la data de las naves")
    try: 
        
        plt.figure(figsize=(14,12))
        plt.barh(data['name'], data['cargo_capacity'], color='green')
        plt.xlabel('Capacidad de carga')
        plt.ylabel('Nombre de la nave')
        plt.title('Comparación de longitud de las naves')
        plt.tight_layout()
        plt.show()

    except:
        print("Error al aplicar la función")
        return(graficos_naves)

def show_graphic4():
    try:
        data = pd.read_csv('CSV/starships.csv')
    except: 
        print("No se ha podido cargar la data de las naves")
    try: 
        
        plt.figure(figsize=(10, 8))
        plt.barh(data['name'], data['hyperdrive_rating'], color='orange')
        plt.xlabel('Clasificación de hiperimpulsor.')
        plt.ylabel('Nombre de la nave')
        plt.title('Comparación de hiperimpulsores')
        plt.xticks((range(0,5,1)))
        plt.tight_layout()
        plt.show()

    except:
        print("Error al aplicar la función")
        return(graficos_naves)

def show_graphic5():
    try:
        data = pd.read_csv('CSV/starships.csv')
    except: 
        print("No se ha podido cargar la data de las naves")
    try: 
        
        plt.figure(figsize=(12, 10))
        plt.barh(data['name'], data['MGLT'], color='yellow')
        plt.xlabel('Modern Galactic Light Time (MGLT)')
        plt.ylabel('Nombre de la nave')
        plt.title('Comparación de MGLT')
        plt.xticks((range(0,125, 5)))
        plt.tight_layout()
        plt.show()

    except:
        print("Error al aplicar la función")
        return(graficos_naves)



def graficos_naves():
    while(True):
        menu = input('''
                        Ingrese el tipo de gráfico sobre las naves que desee visualizar:
                        1._  Longitud de las naves.
                        2._ Capacidad de carga.
                        3._ Clasificación de hiperimpulsor
                        4._ MGLT (Modern Galactic Light Time) 
                        5._ Volver a menú principal
                        6._ Salir                     
                        --> ''')
        if menu== '1':
            show_graphic2()
        elif menu== '2':
            show_graphic3()
        elif menu== '3':
            show_graphic4()
        elif menu== '4':
            show_graphic5()
        elif menu== '5':
            return (menu)
        elif menu== '6':
            break
        
        

        else:
            print('Ingrese una opción valida')


