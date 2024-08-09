def show_species_list(dbspecies, dbplanets, dbfilms, dbcharacters):
    for specie in dbspecies:
        print('\n-----------------')
        planetName = None
        characterNames = []
        episodeNames = []
        for planet in dbplanets:
            if specie.homeworld == planet.url:
                planetName = planet.name
        for urlCharacter in specie.people:
            for character in dbcharacters:
                if urlCharacter == character.url:
                    characterNames.append(character.name)
        for episode in dbfilms:
            for url in episode.species:
                if specie.url == url:
                    episodeNames.append(episode.title)
        specie.show(characterNames,planetName, episodeNames)
        print('-----------------')
