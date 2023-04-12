def movie_organizer(*args):
    movies = dict()
    for name, genre in args:
        if genre not in movies.keys():
            movies[genre] = []
        movies[genre].append(name)
    movies = dict(sorted(movies.items(), key= lambda x: (-len(x[1]), x[0])))
    [names.sort() for names in movies.values()]
    result = []
    for genre, movie_list in movies.items():
        result.append(f"{genre} - {len(movie_list)}")
        [result.append(f"* {movie_name}") for movie_name in movie_list]
    return '\n'.join(result)
