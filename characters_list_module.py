from funciones import cargar_info

def buscar_personaje(dbcharacters):
        entrada_usuario = input("Introduce el nombre del personaje o parte de él: ")
        personajes_filtrados = [character for character in dbcharacters if entrada_usuario.lower() in character.name.lower()]
    
        for character in personajes_filtrados:
            character.show()