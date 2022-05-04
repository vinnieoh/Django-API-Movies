from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .ultls import request_movie
from .serializers import MovieSerializers
from .models import Movie

class MovieSearchAPIView(APIView):
    ...


class MovieListAPIView(generics.ListAPIView):
    ...



class MovieDestroyAPIView(generics.DestroyAPIView):
    ...
