def asignar_starships(dbstarships, urlCharacter):
    starships=[]
    for starship in dbstarships:
        listPeople = starship.pilots
        for people in listPeople:
            if people == urlCharacter:
                starships.append(starship.name)
    return starships