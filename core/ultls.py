import os
import requests


KEY = os.environ.get('API_KEY')

MOVIE_SEARCH_ENDPOINT =  'http://www.omdbapi.com/?i=tt3896198&apikey=' + KEY


def request_movie(movie='100'):
    
    request_movie = requests.get(MOVIE_SEARCH_ENDPOINT + '&t=' + movie).json()

    return request_movie

