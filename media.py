import webbrowser


class Movie():
    """A model of a Movie"""

    def __init__(self, movie_title, storyline, poster_image, trailer_youtube):
        """Initialize title, storyline, poster_image, and trailer attributes"""
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open webbrowser at specified trailer URL"""
        webbrowser.open(self.trailer_youtube_url)
