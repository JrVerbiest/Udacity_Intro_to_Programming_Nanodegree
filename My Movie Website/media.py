"""
    Author: J. Verbiest
    Last update: 19 December 2017
"""

import webbrowser

class Movie():
    """
        This class provides a way to store movie related information.
    """

    def __init__(self, movie_title, poster_image, trailer_youtube, movie_release_data, genre):
        """
        This function generate an instance of the class Movie.

        :param movie_title: title of the movie
        :param poster_image: url of the poster image
        :param trailer_youtube: youtube url of the trailer
        :param movie_release_data: the relaese date of the movie
        :param genre: the genre of the movie
        """
        # initialize instance of class Movie
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_release = movie_release_data
        self.movie_genre = genre

    def show_trailer(self):
        """
        This function playes the trailer of the movie.

        :return: none
        """
        webbrowser.open(self.trailer_youtube_url)

#[EOF]