# Generated by Django 3.1.2 on 2020-10-06 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('spotify_name', models.CharField(blank=True, max_length=50)),
                ('deezer_name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spotify_id', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=100)),
                ('artist', models.TextField(max_length=100)),
                ('image_src', models.URLField()),
                ('platform', models.CharField(choices=[('S', 'Spotify'), ('D', 'Deezer')], default='S', max_length=1)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main-app.genre')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main-app.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main-app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main-app.genre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main-app.profile')),
            ],
        ),
    ]
