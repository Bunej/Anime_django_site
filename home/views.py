from django.shortcuts import render, redirect, get_object_or_404
from .models import Anime, Episode, Comment
from .forms import CommentForm
from accounts.models import UserProfile



def index(request):
    ongoing = Anime.objects.order_by('title')
    date = Anime.objects.order_by('-add_date')
    e_date = Episode.objects.order_by('-add_date')
    context = {'ongoing': ongoing, 'date': date, 'e_date': e_date}
    return render(request, 'home/home.html', context)


def anime_title(request, slug):
    anime = Anime.objects.get(slug=slug)
    episode = Episode.objects.filter(series=anime).order_by('-add_date')
    comment = Comment.objects.filter(anime=anime)
    context = {'anime': anime, 'episode': episode, 'comment': comment}
    return render(request, 'home/anime_detail.html', context)


def add_comment(request, slug):
    anime = get_object_or_404(Anime, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.anime = anime
            comment.user = request.user.userprofile
            comment.save()
            return redirect('anime_title', slug=slug)
    else:
        form = CommentForm()
        context = {'form': form}
        return render(request, 'home/add_comment.html', context)


def edit_comment(request, slug, id=None):
    anime = get_object_or_404(Anime, slug=slug)
    comment = get_object_or_404(Comment, id=id)
    form = CommentForm(request.POST, instance=comment)
    if request.method == 'POST' or 'GET':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.anime = anime
            comment.body
            comment.save()
            return redirect('anime_title', slug=slug)
        else:
            form = CommentForm()
            context = {'form': form}
            return render(request, 'home/edit-comment.html', context)


def delete_comment(request, slug , id=None):
    anime = get_object_or_404(Anime, slug=slug)
    comment = get_object_or_404(Comment, id=id)
    if request.method == 'GET':
        comment.delete()
        return redirect('anime_title', slug=slug)