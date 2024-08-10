characters_in_planets= {}

personajes = show_characters()
for character in charecters:
    planeta_origen = personaje["properties"]["homeworld"]
    if planeta_origen in personajes_por_planeta:
        personajes_por_planeta[planeta_origen] += 1
    else:
        personajes_por_planeta[planeta_origen] = 1