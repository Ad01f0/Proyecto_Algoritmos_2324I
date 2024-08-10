def asignar_species(dbspecies, urlCharacter):
    for specie in dbspecies:
        listPeople = specie.people
        for people in listPeople:
            if people == urlCharacter:
                return specie.name
    return "No indentificado"