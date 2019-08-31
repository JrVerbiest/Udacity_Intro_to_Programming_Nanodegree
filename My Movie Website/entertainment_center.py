"""
    Author: J. Verbiest
    Last update: 19 December 2017
"""

import media
import fresh_tomatoes
import json

# Read movie data from the json file
data = json.load(open('myMovieList.json'))

# generate the movie objects
movies = []
for movie in range(1, len(data)+1):
    movie_title= data["movie_"+str(movie)]["image_title"]
    movie_poster_url= data["movie_"+str(movie)]["image_url"]
    movie_trailer_url = data["movie_"+str(movie)]["trailer_youtube_url"]
    movie_release = data["movie_" + str(movie)]["movie_release_year"]
    movie_genre = data["movie_" + str(movie)]["movie_genre"]

    movies.append(media.Movie(movie_title, movie_poster_url, movie_trailer_url, movie_release, movie_genre))

# generate the html page.
# input is a list of movies
fresh_tomatoes.open_movies_page(movies)

#[EOF]