from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics

from .models import GamesList
from .serializers import GamesListSerializer
from rest_framework import filters


class GamesListing(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = GamesList.objects.all()
    serializer_class = GamesListSerializer


class GamesDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = GamesList.objects.all()
    serializer_class = GamesListSerializer


class GamesDetailsSearch(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = GamesList.objects.all()
    serializer_class = GamesListSerializer  
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'platform', 'genre', 'editors_choice']