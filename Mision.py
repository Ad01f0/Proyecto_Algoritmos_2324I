#crear misión

class Mision:
    def __init__(self, nombre, planeta, aeronave, armas, integrantes, nombredeusuario, CIusuario ):
        self.nombre=nombre
        self.planeta=planeta
        self.aeronave=aeronave
        self.armas=armas
        self.integrantes=integrantes
        self.nombredeusuario=nombredeusuario
        self.CIusuario=CIusuario

def __str__(self):
        return (f'''Nombre de la misión: {self.nombre}
                Planeta destino: {self.planeta}
                Nave: {self.nave}
                Armas: {', '.join(self.armas)}
                Integrantes: {', '.join(self.integrantes)}''')
    
def seleccionar_armas():
        armas = []
        print("Ingrese las armas que desea utilizar (máximo 7).")
        #print lista de armas
        for numero in range(7):
            arma = input(f"Arma {numero+1}: ")
            armas.append(arma)
            if numero < 6:
                continuar = input("¿Desea agregar otra arma? (si/no): ").lower()
                if continuar != 'si':
                    break
        return armas
    
def seleccionar_integrantes():
        integrantes = []
        print("Ingrese los integrantes de la misión (máximo 7).")
        #print lista de characters
        for numero in range(7):
            integrante = input(f"Integrante {numero+1}: ")
            integrantes.append(integrante)
            if numero < 6:
                continuar = input("¿Desea agregar otro integrante? (si/no): ").lower()
                if continuar != 'si':
                    break
        return integrantes

def crear_misiones():
        misiones = []
        for numero in range(5):
            print(f"Creando la misión {numero+1}")
            nombre = input("Ingrese el nombre de la misión: ")
            #lista de planetas
            planeta = input("Ingrese el planeta destino: ")
            #lista de naves
            nave = input("Ingrese la nave a utilizar: ")

            armas = seleccionar_armas()
            integrantes = seleccionar_integrantes()

            mision = Mision(nombre, planeta, nave, armas, integrantes)
            misiones.append(mision)

            if numero < 4:
                continuar = input("¿Desea crear otra misión? (si/no): ").lower()
                if continuar != 'si':
                    break
        
        return misiones

def main():
    misiones = crear_misiones()
    
    print("\nMisiones creadas:")
    for mision in misiones:
        print("\n" + str(mision))


if __name__ == "__main__":
    main()