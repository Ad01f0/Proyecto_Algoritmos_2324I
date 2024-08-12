def asignar_planeta(dbplanetas, urlPlanet): #Recorre la lista de planetas y verifica si el URL del planeta coincide con alguno en la lista. 
    for planeta in dbplanetas:
        if planeta.url == urlPlanet:
            return planeta.name
    return "Desconocido"