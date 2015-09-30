import media
import fresh_tomatoes

aMovie=media.Movie("Forest Gump", 
	"Fanastic story",
	"https://www.movieposter.com/posters/archive/main/41/MPW-20583",
	"www.youtube.com/watch?v=uPIEn0M8su0")

bMovie=media.Movie("Lord Of the Rings",
	"Fantasy",
	"https://www.movieposter.com/posters/archive/main/16/MPW-8295",
	"https://www.youtube.com/watch?v=Pki6jbSbXIY")

#print(aMovie.title)
#aMovie.show_trailer()
fresh_tomatoes.open_movies_page([aMovie, bMovie])
print(media.Movie.__doc__)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__module__)
print(media.Movie.__name__)