from django import forms
from .models import Comment, Anime, Episode


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'body',
        )


class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = (
            'title',
            'ongoing',
            'ended',
            'slug',
            'genre_audience',
            'genre',
        )


class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = (
            'series',
            'number',
            'url',
        )
