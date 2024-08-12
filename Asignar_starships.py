def asignar_starships(dbstarships, urlCharacter):
    starships=[]
    for starship in dbstarships:
        listPeople = starship.pilots
        for people in listPeople:
            if people == urlCharacter:
                starships.append(starship.name)
    if len(starships) > 0:
        return starships
    else:
        return "No tiene naves."