# Generated by Django 3.2.4 on 2021-06-11 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionsAnswers', '0002_questionslist_complexity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topplayer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='points',
            name='commonPoints',
        ),
        migrations.RemoveField(
            model_name='points',
            name='numberGames',
        ),
        migrations.DeleteModel(
            name='AnswerOption',
        ),
        migrations.DeleteModel(
            name='TopPlayer',
        ),
    ]
