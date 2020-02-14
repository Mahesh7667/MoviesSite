from django.db import models

# Create your models here.

GENRE_CHOICES = (

    ('A' , "ACTION"),
    ('C' , "COMEDY"),
    ('D',"DRAMA"),
)
LANG_CHOICES = (

    ('EN', "ENGLISH"),
)


class MovieModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movies')
    genre = models.CharField(choices=GENRE_CHOICES , max_length=1)
    lang = models.CharField(choices=LANG_CHOICES , max_length= 2)
    year = models.DateField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title