cinema_genres = ["комедия", "экшен", "пеплум", "триллер", "комедия", "пеплум"]

set_cinema_genres = set(cinema_genres)
print('set cinema genres - ', set_cinema_genres)
set_cinema_genres.update(['фантастика', 'документальный'])
print('set cinema genres add - ', set_cinema_genres)
set_cinema_genres.discard('экшен')
print('set cinema genres discard - ', set_cinema_genres)
set_cinema_genres.pop()
print('set cinema genres pop - ', set_cinema_genres)
print(list(set_cinema_genres))
