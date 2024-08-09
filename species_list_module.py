def show_species_list(dbspecies):
    for specie in dbspecies:
        print('\n-----------------')
        specie.show()
        print('-----------------')