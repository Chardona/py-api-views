from django.db import models


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return f"{self.name}"


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(to=Actor)
    genres = models.ManyToManyField(to=Genre)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.title}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return f"{self.name}: {self.rows * self.seats_in_row} seats"
