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
            if planet.name == character.homeworld:
                homeworldCharacters.append(character.name)
        planet.show(filmNames, homeworldCharacters)
        print('-----------------')