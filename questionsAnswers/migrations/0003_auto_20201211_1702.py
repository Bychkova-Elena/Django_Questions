# Generated by Django 3.1.4 on 2020-12-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionsAnswers', '0002_auto_20201211_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionslist',
            name='clarification',
            field=models.TextField(null=True, verbose_name='Clarification'),
        ),
    ]
