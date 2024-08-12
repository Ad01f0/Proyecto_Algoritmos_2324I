def show_planets_list(dbplanets, dbfilms, dbcharacters):
    for planet in dbplanets:
        print('\n-----------------')
        filmNames = []
        homeworldCharacters = []
        for film in dbfilms:
            for url in film.planet:
                if planet.url == url:
                    filmNames.append(film.title)
        for character in dbcharacters:
                if character.homeworld == planet.url:
                    homeworldCharacters.append(character.name)
        planet.show(filmNames,homeworldCharacters)
        print('-----------------')

#Muestra una lista de planetas, las películas en las que aparecen y los personajes originarios de cada planeta.