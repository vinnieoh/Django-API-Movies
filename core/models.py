from django.db import models


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)

    class Meta:
        abstract = True


class Movie(Base):
    Title = models.CharField(max_length=200)
    Year = models.CharField(max_length=200)
    Rated = models.CharField(max_length=200)
    Released = models.CharField(max_length=200)
    Runtime = models.CharField(max_length=200)
    Genre = models.CharField(max_length=200)
    Director = models.CharField(max_length=200)
    Writer = models.CharField(max_length=1500)
    Actors = models.CharField(max_length=1500)
    Plot = models.CharField(max_length=1500)
    Language = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    Awards = models.CharField(max_length=200)
    Poster = models.CharField(max_length=1500)
    Metascore = models.CharField(max_length=200)
    imdbRating = models.CharField(max_length=200)
    imdbVotes = models.CharField(max_length=200)
    imdbID = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    totalSeasons = models.CharField(max_length=200)
    DVD = models.CharField(max_length=100)
    BoxOffice = models.CharField(max_length=100)
    Production = models.CharField(max_length=100)
    Website = models.CharField(max_length=100)
    Response = models.CharField(max_length=200)

    def __str__(self):
        return f'Titulo: {self.Title} | ID: {self.id}'


