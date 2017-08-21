import media
import fresh_tomatoes

toy_story = media.Movie(
    "Toy Story",
    "some crap",
    "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",  # NOQA
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")
different = media.Movie(
    "And now for something completely different",
    "yurp",
    "https://static1.squarespace.com/static/5342b8d7e4b0cc3fc1bc6079/t/577af0fe197aea2767b508bf/1467674907628/",  # NOQA
    "https://www.youtube.com/watch?v=IDtepG8EvHE")
producers = media.Movie(
    "Producers",
    "blargh",
    "https://alchetron.com/cdn/The-Producers-1968-film-images-a70bb3a4-4655-4fd1-b4ea-5ef6012ebbf.jpg?op=OPEN",  # NOQA
    "https://www.youtube.com/watch?v=pTW2ZSjG5N0")

movie_list = [toy_story, different, producers]
fresh_tomatoes.open_movies_page(movie_list)
