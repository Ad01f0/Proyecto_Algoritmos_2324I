def asignar_planeta(dbplanetas, urlPlanet):
    for planeta in dbplanetas:
        if planeta.url == urlPlanet:
            return planeta.name
    return "Desconocido"