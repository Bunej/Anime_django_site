from django.db import models
from multiselectfield import MultiSelectField
from accounts.models import UserProfile


class Anime(models.Model):
    title = models.CharField(max_length=300, unique=True)
    ongoing = models.BooleanField(default=True)
    ended = models.BooleanField(default=False)
    add_date = models.DateTimeField('Date added')
    slug = models.SlugField()
    genre_audience_choices = (('genre_audience_choice1', 'Shounen'),
                              ('genre_audience_choice2', 'Seinen'),
                              )
    genre_audience = MultiSelectField(choices=genre_audience_choices, max_choices=2)
    genre_choices = (('genre_choice1', 'Action'),
                     ('genre_choice2', 'Adventure'),
                     ('genre_choice3', 'Comedy'),
                     ('genre_choice4', 'Drama'),
                     ('genre_choice5', 'Fantasy'),
                     ('genre_choice6', 'Horror'),
                     ('genre_choice7', 'Martial Arts'),
                     ('genre_choice8', 'Mystery'),
                     ('genre_choice9', 'Super Power'),
                     ('genre_choice10', 'Supernatural'),
                     )
    genre = MultiSelectField(choices=genre_choices, max_choices=10)

    def __str__(self):
        return self.title


class Episode(models.Model):
    series = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name='Series')
    number = models.CharField('Episode Number', max_length=5)
    url = models.URLField('Episode url')
    add_date = models.DateTimeField('date added')

    def __str__(self):
        return self.series.title + ' ' + self.number


class Comment(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' ' + self.body + ' ' + str(self.anime)
