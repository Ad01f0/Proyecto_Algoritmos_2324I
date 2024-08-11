class Mision:
    def __init__(self, nombre, planeta, nave, armas, integrantes):
        self.nombre = nombre
        self.planeta = planeta
        self.nave = nave
        self.armas = armas
        self.integrantes = integrantes

    def __str__(self):
        return (f"Nombre de la misión: {self.nombre}\n"
                f"Planeta destino: {self.planeta}\n"
                f"Nave: {self.nave}\n"
                f"Armas: {', '.join(self.armas)}\n"
                f"Integrantes: {', '.join(self.integrantes)}")

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
                self.planeta = input("Ingrese el nuevo planeta destino: ")
            elif opcion == '3':
                self.nave = input("Ingrese la nueva nave a utilizar: ")
            elif opcion == '4':
                self.armas = seleccionar_armas()
            elif opcion == '5':
                self.integrantes = seleccionar_integrantes()
            elif opcion == '6':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

# Función para seleccionar armas
def seleccionar_armas():
    armas = []
    print("Ingrese las armas que desea utilizar (máximo 7).")
    for i in range(7):
        arma = input(f"Arma {i+1}: ")
        armas.append(arma)
        if i < 6:
            continuar = input("¿Desea agregar otra arma? (s/n): ").lower()
            if continuar != 's':
                break
    return armas

# Función para seleccionar integrantes
def seleccionar_integrantes():
    integrantes = []
    print("Ingrese los integrantes de la misión (máximo 7).")
    for i in range(7):
        integrante = input(f"Integrante {i+1}: ")
        integrantes.append(integrante)
        if i < 6:
            continuar = input("¿Desea agregar otro integrante? (s/n): ").lower()
            if continuar != 's':
                break
    return integrantes

# Función para crear misiones
def crear_misiones():
    misiones = []
    for i in range(5):
        print(f"\nCreando la misión {i+1}")
        nombre = input("Ingrese el nombre de la misión: ")
        planeta = input("Ingrese el planeta destino: ")
        nave = input("Ingrese la nave a utilizar: ")

        armas = seleccionar_armas()
        integrantes = seleccionar_integrantes()

        mision = Mision(nombre, planeta, nave, armas, integrantes)
        misiones.append(mision)

        if i < 4:
            continuar = input("¿Desea crear otra misión? (s/n): ").lower()
            if continuar != 's':
                break
    
    return misiones

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
    if not misiones:
        print("No hay misiones para visualizar.")
        return

    print("Misiones disponibles:")
    for i, mision in enumerate(misiones):
        print(f"{i+1}. {mision.nombre}")

    seleccion = int(input("Seleccione el número de la misión que desea visualizar: ")) - 1

    if 0 <= seleccion < len(misiones):
        print("\nDetalles de la misión seleccionada:")
        print(misiones[seleccion])
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
def main():
    misiones = []
    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear misión")
        print("2. Modificar misión")
        print("3. Visualizar misión")
        print("4. Guardar misiones")
        print("5. Cargar misiones")
        print("6. Salir")
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
            misiones = cargar_misiones()
        elif opcion == '6':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecuta el sistema
if __name__ == "__main__":
    main()