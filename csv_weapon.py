import csv 

class Weapon:
   def __init__(self, id, name): 
    self.id = id
    self.name = name

   ruta = "C:\\Users\\gabyp\\Documents\\proyecto_algoritmos\\starwars\\weapons.csv"

   def weapons_from_csv(ruta_archivo):
      weapons = []
      with open(ruta_archivo, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            weapon = Weapon(
                row['id'],
                row['name'],
            )
            weapons.append(weapon)
            return weapons
   
   def select_weapon(weapons):
    try:
        opcion = int(input("Seleccione un arma: "))
        eleccion_arma = weapons[opcion - 1]
        print(f'Has seleccionado el arma {eleccion_arma.name}.')
        return eleccion_arma
    except:
        print("Carácter inválido. Inténtalo nuevamente.")
        
        def show_weapons(weapons):
          print("Lista de armas:")
        for i, weapon in enumerate(weapons, 1):
          print(f'{i}. {weapon.name}')

 
