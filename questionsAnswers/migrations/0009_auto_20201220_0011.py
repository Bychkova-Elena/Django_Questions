# Generated by Django 3.1.4 on 2020-12-19 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionsAnswers', '0008_topplayer_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topplayer',
            name='points',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.PROTECT, to='questionsAnswers.points', verbose_name='Points'),
        ),
    ]
