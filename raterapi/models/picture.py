from django.db import models
from django.contrib.auth.models import User


class Pictures(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pictures_added')
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='pictures')
    image = models.ImageField(
        upload_to='pictures/',
        height_field=None,
        width_field=None,
        max_length=100
        )