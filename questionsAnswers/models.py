from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    # Категории #

    nameCategory = models.CharField(max_length=150)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Subcategory(models.Model):
    # Подкатегории #

    nameSubcategory = models.CharField(max_length=150)
    category = models.ForeignKey(Category)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'


class Question(models.Model):
    # Вопросы #

    question = models.TextField()
    subcategory = models.ForeignKey(Subcategory)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Answer(models.Model):
    # Ответы #

    answer = models.TextField()
    clarification = models.TextField()
    question = models.OneToOneField()

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'


class AnswerOption(models.Model):
    # Варианты ответов #

    option = models.TextField()
    question = models.ForeignKey(Question)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'AnswerOption'
        verbose_name_plural = 'AnswerOptions'


class Complaint(models.Model):
    # Жалобы #

    complaint = models.TextField()
    status = models.BooleanField()
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Complaint'
        verbose_name_plural = 'Complaints'


class Point(models.Model):
    # Баллы #

    quantity = models.PositiveIntegerField()
    numberGames = models.PositiveIntegerField()
    commonPoints = models.PositiveIntegerField()
    user = models.OneToOneField(User)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Point'
        verbose_name_plural = 'Points'


class TopPlayer(models.Model):
    # Лучшие игроки #

    user = models.OneToOneField(User)
    poins = models.OneToOneField(Point)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'TopPlayer'
        verbose_name_plural = 'TopPlayers'


class News(models.Model):
    # Новости для блога #

    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'News'
        verbose_name_plural = 'News'
