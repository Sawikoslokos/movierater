from django.db import models


class ExtraInfo(models.Model):
    rodzaje = {
        (0, 'Nieznany'),
        (1, 'Dramat'),
        (2, 'Sci-Fi'),
        (3, 'Komedia')
    }

    czas_trwania = models.IntegerField()
    rodzajFilmu = models.IntegerField(choices=rodzaje)


class Film(models.Model):
    tytul = models.CharField(max_length=32)
    opis = models.TextField(max_length=256, null=True, blank=True)
    po_premierze = models.BooleanField(default=False)
    premiera = models.DateField(null=True, blank=True)
    rok = models.IntegerField()
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    extrainfo = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.tytul + " (" + str(self.rok) + ")"


class Recenzja(models.Model):
    opis = models.TextField(default='')
    gwiazdki = models.IntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='recenzje')


class Aktor(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    filmy = models.ManyToManyField(Film, related_name='aktorzy')

    def __str__(self):
        return self.imie + " " + self.nazwisko
