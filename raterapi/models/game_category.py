from django.db import models


class GameCategory(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)



