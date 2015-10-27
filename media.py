import webbrowser


class Movie(object):
	"""Movie class.

    Describes attributes of a movie.

    Attributes:
        title (str): movie title.
        poster_image_url (str): url for movie poster poster_image.
        trailer_youtube_url (str): url for movie trailer.
        movie_stars (str): string of stars in the movie.
    """

	def __init__(
			self, movie_title, poster_image_url,
			trailer_youtube_url, movie_stars):
		"""returns a Movie object with all its attributes
		assigned to arguments passed in"""
		self.title = movie_title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.movie_stars = movie_stars
