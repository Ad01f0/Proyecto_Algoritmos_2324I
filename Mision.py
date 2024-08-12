from csv_planet import planets
from csv_characters import characters
from csv_ships import starchips
from csv_weapon import weapons
class Mision:
    def __init__(self, nombre, planeta, nave, armas, integrantes):
        self.nombre = nombre
        self.planeta = planeta
        self.nave = nave
        self.armas = armas
        self.integrantes = integrantes

    def __str__(self):
        return (f"Nombre de la mision: {self.nombre}\n"
                f"Planeta destino: {self.planeta}\n"
                f"Nave: {self.nave}\n"
                f"Armas: {', '.join(self.armas)}\n"
                f"Integrantes: {', '.join(self.integrantes)}")

    def show(self, nave, armas_info, integrantes_info):
        print(f"Nombre de la mision: {self.nombre}\n")
        print(f"Planeta destino: {self.planeta}\n")
        print('-----Nave-----\n')
        print(f"{nave.show()}\n\n")
        print('-----Armas-----\n')
        for arma in armas_info:
            print(f"{arma.show()}\n\n")
        print('-----Integrantes-----')
        for integrante in integrantes_info:
            print(f"{integrante.show()}\n\n")

    def modificar_mision(self):
        while True:
            print("\n¿Qué desea modificar?")
            print("1. Nombre de la misión")
            print("2. Planeta destino")
            print("3. Nave a utilizar")
            print("4. Modificar armas")
            print("5. Modificar integrantes")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.nombre = input("Ingrese el nuevo nombre de la misión: ")
            elif opcion == '2':
                
                self.planeta = modificar_planeta(self.planeta)
                
            elif opcion == '3':
                self.nave = modificar_nave(self.nave)
            elif opcion == '4':
                self.armas = modificar_armas(self.armas)
            elif opcion == '5':
                self.integrantes = modificar_integrantes(self.integrantes)
            elif opcion == '6':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

# Función para seleccionar armas
def seleccionar_armas(armas_seleccionadas):
    armas = []
    if len(armas_seleccionadas) > 0:
        armas = armas_seleccionadas
    print("Armas disponibles para la misión:")
    for weapon in weapons:
            print(f"{weapon.id}.- {weapon.name}")
    print("Ingrese las armas que desea utilizar (máximo 7).")
    while(True):
        if len(armas) < 7: 
            arma = int(input(f"Arma {len(armas)+1}: "))
            if arma > 60:
                print('Ingrese una opcion valida')
            else:
                for weapon in weapons:
                    if arma == weapon.id:
                        armas.append(weapon.name) 
                        while(True):    
                            if len(armas) < 7:
                                continuar = input("¿Desea agregar otra arma? (si/no): ").lower()
                                if continuar == 'no':
                                    return armas
                                elif continuar == 'si': 
                                    break
                                else:
                                    print("Ingresa una opcion valida.")
                            else:
                                print("\nYa no se pueden agregar mas armas.")
                                return armas
        else:
            print('Ya no se pueden agregar mas armas.')
            break

def modificar_armas(armas_seleccionadas):
    armas = armas_seleccionadas
    while(True):
        print("\n1. Agregar armas")
        print("2. Eliminar armas")
        print("3. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            armas = seleccionar_armas(armas)
        elif opcion =='2':
            if len(armas) > 0:
                while(True):
                    
                    print("\nQue arma deseas eliminar?")
                    for i, arma in enumerate(armas):
                        print(f"{i+1}.- {arma}")

                    eliminar = int(input('Selecciona una opcion: \n'))
                    if eliminar > len(armas):
                        print('\nSelecciona una opcion valida.\n')
                    else:
                        texto = armas[eliminar-1]
                        armas.pop(eliminar-1)
                        print(f"{texto} ha sido eliminada correctamente.\n")
                        break
            else:
                print('\nNo hay armas agregadas a la mision.\n')
        elif opcion =='3':
            return armas
        else:
            print('\nIngrese una opcion valida\n')
            
# Función para seleccionar integrantes
def seleccionar_integrantes(integrantes_seleccionados):
    integrantes = []
    if len(integrantes_seleccionados) > 0:
        integrantes = integrantes_seleccionados
    print(integrantes)
    print("Personajes disponibles para la misión:")
    for character in characters:
         print(f"{character.id}.- {character.name}")
    print("Ingrese los integrantes de la misión (máximo 7).")
    while(True):
        boolean = True
        if len(integrantes) < 7: 
            integrante = int(input(f"Integrante {len(integrantes)+1}: "))
            if integrante > 96:
                print("Ingrse una opcion valida")
            else:
                for i in integrantes:
                    for character in characters:
                        if integrante == character.id:
                            if i == character.name:
                                print("\nNo puedes repetir personajes.\n")
                                boolean = False
                if boolean == True:
                    for character in characters:
                        if integrante == character.id:
                            integrantes.append(character.name)
                            while(True):
                                if len(integrantes) < 7:
                                    continuar = input("¿Desea agregar otro personaje? (si/no): ").lower()
                                    if continuar == 'no':
                                        return integrantes
                                    elif continuar == 'si': 
                                        break
                                    else:
                                        print("Ingresa una opcion valida.")
                                else:
                                    print("\nYa no se pueden agregar mas personajes.")
                                    return integrantes
        else:
            print('Ya no se puedes agregar mas integrantes.')
            break

def modificar_integrantes(integrantes_seleccionados):
    integrantes = integrantes_seleccionados
    while(True):
        print("\n1. Agregar integrantes")
        print("2. Eliminar integrantes")
        print("3. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            integrantes = seleccionar_integrantes(integrantes)
        elif opcion =='2':
            if len(integrantes) > 0:
                while(True):
                    print("\nQue integrantes deseas eliminar?")
                    for i, integrante in enumerate(integrantes):
                        print(f"{i+1}.- {integrante}")
                    eliminar = int(input('Selecciona una opcion: \n'))
                    if eliminar > len(integrantes):
                        print('\nSelecciona una opcion valida.\n')
                    else:
                        texto = integrantes[eliminar-1]
                        integrantes.pop(eliminar-1)
                        print(f"{texto} ha sido eliminado correctamente.\n")
                        break
            else:
                print('\nNo hay armas integrantes a la mision.\n')
        elif opcion =='3':
            return integrantes
        else:
            print('\nIngrese una opcion valida\n')

#funcion para seleccionar planeta
def seleccionar_planeta():
    while(True):
        print("Planetas disponibles para la misión:")
        for planet in planets:
            print(f"{planet.id}.- {planet.name}")
        planeta = int(input("Ingrese el planeta destino: "))
        for planet in planets:
            if planeta == planet.id:
                return planet.name
        if planeta > 13:
            print('\nIngrese una opción válida\n') 

#funcion para modificar planeta
def modificar_planeta(planeta_seleccionado):
    while(True):
        print("Planetas disponibles para la misión:")
        for planet in planets:
            print(f"{planet.id}.- {planet.name}")
        new_planet = int(input("Ingrese el planeta destino: "))
        for planet in planets:
            if new_planet == planet.id:
                if planet.name == planeta_seleccionado:
                    print('No puedes seleccionar el mismo planeta.')
                else:
                    return planet.name
        if new_planet > 13:
            print('\nIngrese una opción válida\n') 

#Funcion para seleccionar naves 
def seleccionar_nave():
    while(True):
        print("Naves disponibles para la misión:")
        for starship in starchips:
            print(f"{starship.id}.- {starship.name}")
        nave = int(input("Ingrese la nave a utilizar: "))
        for starship in starchips:
            if nave == starship.id:
                return starship.name
        if nave > 60:
            print ("\nIngrese una opcion valida\n")
            

def modificar_nave(nave_seleccionada):
    while(True):
        print("Naves disponibles para la misión:")
        for starship in starchips:
            print(f"{starship.id}.- {starship.name}")
        new_starship = int(input("Ingrese la nueva nave: "))
        for starship in starchips:
            if new_starship == starship.id:
                if starship.name == nave_seleccionada:
                    print('\nNo puedes seleccionar la misma nave.\n')
                else:
                    return starship.name
        if new_starship > 60:
            print('\nIngrese una opción válida\n') 
            
    

# Función para crear misiones
def crear_misiones():
    misiones = []
    while(True):
        if len(misiones) < 5:
            print(f"\nCreando la misión {len(misiones)+1}")
            nombre = input("Ingrese el nombre de la misión: ")
            planeta = seleccionar_planeta()
            nave= seleccionar_nave()
            armas = seleccionar_armas([])
            integrantes = seleccionar_integrantes([])

            mision = Mision(nombre, planeta, nave, armas, integrantes)
            misiones.append(mision)
            while(True):
                if len(misiones) < 5:
                    continuar = input("¿Desea crear otra misión? (si/no): ").lower()
                    if continuar == 'no':
                        return misiones
                    elif continuar == 'si':
                        break
                    else: 
                        print("Ingrese una opcion valida")
                else:
                    print('No puedes crear mas de 5 misiones.')
                    return misiones
        else:
            print('No puedes crear mas de 5 misiones.')
            break        
    

# Función para modificar una misión existente
def modificar_mision(misiones):
    if not misiones:
        print("No hay misiones para modificar.")
        return

    print("Misiones disponibles:")
    for i, mision in enumerate(misiones):
        print(f"{i+1}. {mision.nombre}")

    seleccion = int(input("Seleccione el número de la misión que desea modificar: ")) - 1

    if 0 <= seleccion < len(misiones):
        misiones[seleccion].modificar_mision()
    else:
        print("Selección no válida.")

# Función para visualizar una misión
def visualizar_mision(misiones):
    while(True):
        if not misiones:
            print("No hay misiones para visualizar.")
            break
        print("Misiones disponibles:")
        for i, mision in enumerate(misiones):
            print(f"{i+1}. {mision.nombre}")

        seleccion = int(input("Seleccione el número de la misión que desea visualizar: ")) - 1

        if 0 <= seleccion < len(misiones):
            nave = misiones[seleccion].nave
            armas = misiones[seleccion].armas
            integrantes = misiones[seleccion].integrantes

            armas_info = []
            integrantes_info = []

            for starship in starchips:
                if nave == starship.name:
                    nave = starship
            for arma in armas:
                for weapon in weapons:
                    if arma == weapon.name:
                        armas_info.append(weapon)
            for integrante in integrantes:
                for character in characters:
                    if integrante == character.name:
                        integrantes_info.append(character)

            print("\nDetalles de la misión seleccionada:")
            print(misiones[seleccion].show(nave,armas_info,  integrantes_info))
            break
        else:
            print("Selección no válida.")

# Función para guardar misiones en un archivo de texto
def guardar_misiones(misiones, filename="dbmisiones.txt"):
    with open(filename, 'w') as archivo:
        for mision in misiones:
            archivo.write(str(mision) + "\n\n")
    print(f"Misiones guardadas en {filename}")

# Función para cargar misiones desde un archivo de texto
def cargar_misiones(filename="dbmisiones.txt"):
    misiones = []
    try:
        with open(filename, 'r') as archivo:
            contenido = archivo.read().strip().split("\n\n")
            for m in contenido:
                if m.strip():
                    datos = m.split('\n')
                    nombre = datos[0].split(": ")[1]
                    planeta = datos[1].split(": ")[1]
                    nave = datos[2].split(": ")[1]
                    armas = datos[3].split(": ")[1].split(", ")
                    integrantes = datos[4].split(": ")[1].split(", ")
                    misiones.append(Mision(nombre, planeta, nave, armas, integrantes))
        print(f"Misiones cargadas desde {filename}")
    except FileNotFoundError:
        print(f"Archivo {filename} no encontrado.")
    
    return misiones

# Función principal del sistema
def misiones():
    misiones = cargar_misiones()

    while True:
        
        print("\n--- Menú Misiones ---")
        print("1. Crear misión")
        print("2. Modificar misión")
        print("3. Visualizar misión")
        print("4. Guardar misiones")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            misiones.extend(crear_misiones())
            
        elif opcion == '2':
           
            modificar_mision(misiones)
        elif opcion == '3':
           
            visualizar_mision(misiones)
        elif opcion == '4':
          
            guardar_misiones(misiones)
        elif opcion == '5':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    # Ejecuta el sistema
    misiones()