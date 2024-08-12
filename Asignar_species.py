def asignar_species(dbspecies, urlCharacter): #Recorre una lista de especies y verifica si el personaje está presente en la lista de personas asociadas a cada especie. 
    for specie in dbspecies:
        listPeople = specie.people
        for people in listPeople:
            if people == urlCharacter:
                return specie.name
    return "No indentificado"