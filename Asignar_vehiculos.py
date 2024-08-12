def asignar_vehiculos(dbvehicles, urlCharacter): #Recorre una lista de vehículos y verifica si el personaje maneja de alguno de ellos.
    vehicles = []
    for vehicle in dbvehicles:
        listPilots = vehicle.pilots
        for pilot in listPilots:
            if pilot == urlCharacter:
                vehicles.append(vehicle.name)
    if len(vehicles) > 0:
        return vehicles
    else:
        return "No tiene vehiculos."