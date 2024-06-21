from django.db import models

# Create your models here.

class Singer(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

class Album(models.Model):
    nombre = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE,blank=False)
    
    def __str__(self):
        return self.nombre

class Song(models.Model):
    nombre = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.nombre