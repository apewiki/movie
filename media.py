import webbrowser

class Movie():
	"""docstring for Media"""

	VALID_RATINGS=['PG','PG13','R'] #class variables
	def __init__(self, movie_title, movie_story, poster_image_url, trailer_youtube_url):
		#super(Movie, self).__init__()
		self.title = movie_title	#instance variable
		self.movie_story = movie_story
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube)
		