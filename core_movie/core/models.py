from django.db import models

class MPAA_Rating(models.Model):
    type = models.CharField(max_length=10)
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.type

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    imgPath = models.ImageField(upload_to='movie_images/')
    duration = models.PositiveIntegerField()  # duration is in minutes
    genre = models.ManyToManyField('Genre')
    language = models.CharField(max_length=100)
    mpaaRating = models.ForeignKey(MPAA_Rating, on_delete=models.CASCADE)
    userRating = models.CharField(max_length=10)  # userRating is a string

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
