def show_movie_list(dbfilms):
    for film in dbfilms:
        print('\n-----------------')
        film.show()
        print('-----------------')
        