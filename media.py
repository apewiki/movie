import webbrowser

class Movie():
	"""Movie class.

	Describes attributes of a movie.

	Attributes:
		title: movie title.
		poster_image_url: url for movie poster poster_image.
		trailer_youtube_url: url for movie trailer.
		movie_stars: string of stars in the movie.
	"""

	# class constructor
	def __init__(self, movie_title, poster_image_url, trailer_youtube_url, movie_stars):
		#instance variables
		self.title = movie_title	
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.movie_stars = movie_stars