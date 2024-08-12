def asignar_films(dbfilms, urlCharacter):
    films = []
    for film in dbfilms:
        listPeople = film.characters
        for character in listPeople:
            if character == urlCharacter:
                films.append(film.title)
    if len(films) > 0:
        return films
    else:
        return "Sin episodios registrados."