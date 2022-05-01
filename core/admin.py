from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class AdminMovie(admin.ModelAdmin):
    list_display = ('Title',
                    'Year',
                    'Rated',
                    'Released',
                    'Runtime',
                    'Genre',
                    'Director',
                    'Writer',
                    'Actors',
                    'Plot',
                    'Language',
                    'Country',
                    'Awards',
                    'Poster',
                    'Metascore',
                    'imdbRating',
                    'imdbVotes',
                    'imdbID',
                    'Type',
                    'totalSeasons',
                    'DVD',
                    'BoxOffice',
                    'Production',
                    'Website',
                    'Response'
                )
