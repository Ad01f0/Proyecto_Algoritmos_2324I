def show_planets_list(dbplanets):
    for planet in dbplanets:
        print('\n-----------------')
        planet.show()
        print('-----------------')
        