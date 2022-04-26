from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from api.serializers import UserSerializer, FilmSerializer, RecenzjeSerializer, AktorSerializer
from .models import Film, Recenzja, Aktor


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_fields = ('tytul', 'opis')

    def get_queryset(self):
        films = Film.objects.all()
        return films



    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FilmSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        film = Film.objects.create(tytul=request.data['tytul'],
                                   opis=request.data['opis'],
                                   po_premierze=request.data['po_premierze'])
        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        film = self.get_object()
        film.tytul = request.data['tytul']
        film.opis = request.data['opis']
        film.po_premierze = request.data['po_premierze']
        film.save()

        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        film = self.get_object()
        film.delete()
        return Response('Usunieto Film')

    @action(detail=True, methods=['post'])
    def premiera(self, request, **kwargs):
        film = self.get_object()
        film.po_premierze = request.data['premiera']
        film.save()

        seliarizer = FilmSerializer(film, many=False)
        return Response(seliarizer.data)


class RatingsViewSet(viewsets.ModelViewSet):
    queryset = Recenzja.objects.all()
    serializer_class = RecenzjeSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer

    @action(detail=True, methods=['post'])
    def dolacz(self, request, **kwargs):
        aktor = self.get_object()
        film = Film.objects.get(id=request.data['film'])
        aktor.filmy.add(film)
        aktor.save()

        serializer = AktorSerializer(aktor, many=False)
        return Response(serializer.data)
