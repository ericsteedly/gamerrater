from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    designer = models.CharField(max_length=255)
    release_year = models.IntegerField(max_length=4)
    number_of_players = models.IntegerField(max_length=2)
    playtime = models.TimeField()
    age = models.IntegerField(max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games_created')