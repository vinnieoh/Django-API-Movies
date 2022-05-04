from django.urls import path

from .views import MovieSearchAPIView, MovieListAPIView, MovieDestroyAPIView 

urlpatterns = [
    path('movie-search', MovieSearchAPIView.as_view(), name='movie-search'),
    path('movie-list', MovieListAPIView.as_view(), name='movie-list'),
    path('movie-destroy', MovieDestroyAPIView.as_view(), name='movie-destroy')
]
