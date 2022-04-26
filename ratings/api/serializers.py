from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Film, ExtraInfo, Recenzja, Aktor


class RecenzjeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recenzja
        fields = ['id', 'opis', 'gwiazdki']


class FilmSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['tytul']


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['czas_trwania', 'rodzajFilmu']


class FullFilmDataSeliarizer(serializers.ModelSerializer):
    extrainfo = ExtraInfoSerializer(many=False, read_only=True)
    recenzje = RecenzjeSerializer(many=True, read_only=True)

    class Meta:
        model = Film
        fields = ['id', 'tytul', 'rok', 'imdb_rating', 'opis', 'po_premierze', 'premiera', 'extrainfo', 'recenzje']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class AktorSerializer(serializers.ModelSerializer):
    filmy = FilmSmallSerializer(many=True, read_only=True)

    class Meta:
        model = Aktor
        fields = ['id', 'imie', 'nazwisko', 'filmy']

"""
    def create(self, validated_data):
        filmy = validated_data["filmy"]
        del validated_data["filmy"]

        aktor = Aktor.objects.create(**validated_data)

        for film in filmy:
            f = Film.objects.create(**film)
            aktor.filmy.add(f)

        aktor.save()
        return aktor
"""

class FilmSerializer(serializers.ModelSerializer):
    recenzje = RecenzjeSerializer(many=True, read_only=True)
    aktorzy = AktorSerializer(many=True, read_only=True)

    class Meta:
        model = Film
        fields = ['id', 'tytul', 'opis', 'po_premierze', 'recenzje', 'aktorzy']
