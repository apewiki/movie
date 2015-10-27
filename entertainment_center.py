import media
import fresh_tomatoes

# List of movies
movies = []

# Add movies to the list
poster_name = "https://www.movieposter.com/posters/archive/main/41/MPW-20583"
movies.append(media.Movie("Forest Gump",
                          poster_name,
                          "www.youtube.com/watch?v=uPIEn0M8su0",
                          "Tom Hank, Robin Wright"))

poster_name = "https://www.movieposter.com/posters/archive/main/16/MPW-8295"
actors = "Elijah Wood, Viggo Mortensen, Orlando Bloom, Cate Blanchett"
movies.append(media.Movie("Lord Of the Rings",
                          poster_name,
                          "https://www.youtube.com/watch?v=Pki6jbSbXIY",
                          actors))

poster_name = ("https://upload.wikimedia.org/wikipedia/en/c/ce/"
               "A_river_runs_through_it_cover.jpg")
movies.append(media.Movie("A River Runs Through It",
                          poster_name,
                          "https://www.youtube.com/watch?v=5Z7yeXtBQMU",
                          "Brad Pitt"))


# Open movie list in browser
fresh_tomatoes.open_movies_page(movies)
