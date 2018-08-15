from django.db import models
from django.utils import timezone

class Videogame(models.Model):
    title = models.CharField(max_length=50)
    platform = models.CharField(max_length=10)
    seller = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='covers/', default='covers/no-image.png')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
