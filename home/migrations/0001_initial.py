# Generated by Django 2.0.2 on 2018-02-21 11:43

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('ongoing', models.BooleanField(default=True)),
                ('ended', models.BooleanField(default=False)),
                ('add_date', models.DateTimeField(verbose_name='Date added')),
                ('slug', models.SlugField()),
                ('genre_audience', multiselectfield.db.fields.MultiSelectField(choices=[('genre_audience_choice1', 'Shounen'), ('genre_audience_choice2', 'Seinen')], max_length=45)),
                ('genre', multiselectfield.db.fields.MultiSelectField(choices=[('genre_choice1', 'Action'), ('genre_choice2', 'Adventure'), ('genre_choice3', 'Comedy'), ('genre_choice4', 'Drama'), ('genre_choice5', 'Fantasy'), ('genre_choice6', 'Horror'), ('genre_choice7', 'Martial Arts'), ('genre_choice8', 'Mystery'), ('genre_choice9', 'Super Power'), ('genre_choice10', 'Supernatural')], max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5, verbose_name='Episode Number')),
                ('url', models.URLField(verbose_name='Episode url')),
                ('add_date', models.DateTimeField(verbose_name='date added')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Anime', verbose_name='Series')),
            ],
        ),
    ]
