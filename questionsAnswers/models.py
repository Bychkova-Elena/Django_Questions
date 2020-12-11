from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    # Категории #

    nameCategory = models.CharField("Category", max_length=150)

    def __str__(self):
        return self.nameCategory

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Subcategory(models.Model):
    # Подкатегории #

    nameSubcategory = models.CharField("Subcategory", max_length=150)
    category = models.ForeignKey(
        Category, verbose_name='Category', on_delete=models.CASCADE)

    def __str__(self):
        return '%s (%s)' % (self.nameSubcategory, self.category)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'


class QuestionsList(models.Model):
    # Вопросы и ответы #

    question = models.TextField("Question")
    answer = models.CharField("Answer", max_length=150)
    clarification = models.TextField("Clarification", blank=True, null=True)
    subcategory = models.ForeignKey(
        Subcategory, verbose_name='Subcategory', on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s (%s)' % (self.question, self.answer, self.subcategory)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'QuestionsList'
        verbose_name_plural = 'QuestionsList'


class AnswerOption(models.Model):
    # Варианты ответов #

    first_option = models.CharField(
        "First option", max_length=150)
    second_option = models.CharField(
        "Second option", max_length=150)
    third_option = models.CharField(
        "Third option", max_length=150, blank=True, null=True)
    fourth_option = models.CharField(
        "Fourth option", max_length=150, blank=True, null=True)
    question = models.OneToOneField(
        QuestionsList, verbose_name='QuestionsList', on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.first_option, self.second_option, self.third_option, self.fourth_option)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'AnswerOption'
        verbose_name_plural = 'AnswerOptions'


class Complaint(models.Model):
    # Жалобы #
    SENT = 'SENT'
    CONSIDERATION = 'UNDER CONSIDERATION'
    REJECT = 'REJECT'
    ACCEPT = 'ACCEPT'
    FIXED = 'FIXED'
    STATUS_CHOICES = [
        (SENT, 'SENT'),
        (CONSIDERATION, 'UNDER CONSIDERATION'),
        (REJECT, 'REJECT'),
        (ACCEPT, 'ACCEPT'),
        (FIXED, 'FIXED')
    ]

    complaint = models.TextField("Complaint")
    status = models.CharField("Status",
                              max_length=20,
                              choices=STATUS_CHOICES,
                              default=SENT)
    question = models.ForeignKey(
        QuestionsList, verbose_name='QuestionsList', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s: %s' % (self.status, self.complaint)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Complaint'
        verbose_name_plural = 'Complaints'


class Points(models.Model):
    # Баллы #

    quantity = models.PositiveIntegerField("Quantity", default=0)
    numberGames = models.PositiveIntegerField(
        "Number of games", default=0)
    commonPoints = models.PositiveIntegerField(
        "Common quantity points", default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s, %s' % (self.quantity, self.numberGames, self.commonPoints)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Points'
        verbose_name_plural = 'Points'


class TopPlayer(models.Model):
    # Лучшие игроки #

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.user)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'TopPlayer'
        verbose_name_plural = 'TopPlayers'


class News(models.Model):
    # Новости для блога #

    title = models.CharField("Title", max_length=250)
    body = models.TextField("News")

    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Comment(models.Model):
    # Комментарии #

    comment = models.TextField("Comment")
    news = models.ForeignKey(
        News, verbose_name='News', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.comment

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
