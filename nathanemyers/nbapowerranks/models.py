from django.db import models

# Create your models here.

class Team(models.Model):
    region = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    conference = models.CharField(max_length=100)
    def __str__(self):
        return self.region + ' ' + self.name

class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team)
    def __str__(self):
        return self.name

class Ranking(models.Model):
    year = models.IntegerField()
    week = models.IntegerField()
    team = models.ForeignKey(Team)
    rank = models.IntegerField()
    summary = models.TextField()
    def __str__(self):
        return str(self.year) + ' week ' + str(self.week) + ': ' + str(self.team) + ' #' + str(self.rank)

