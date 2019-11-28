from django.db import models

# Create your models here.
class GamesList(models.Model):
    title = models.TextField()
    platform = models.TextField()
    score = models.TextField()
    genre = models.TextField()
    editors_choice = models.TextField()

    def __str__(self):
        return self.title