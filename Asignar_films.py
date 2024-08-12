def asignar_films(dbfilms, urlCharacter):  #Crea una lista de títulos de películas a un personaje específico recorriendo una lista de películas y verificando si el personaje aparece 

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