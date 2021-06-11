from django.contrib.auth.models import AbstractUser
from django.db import models
import django.utils.timezone


class User(AbstractUser):

    class Meta:
        db_table = 'users'
        managed = True
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Category(models.Model):
    # Категории #

    nameCategory = models.CharField("Категория", max_length=150)

    def __str__(self):
        return self.nameCategory

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    # Подкатегории #

    nameSubcategory = models.CharField("Подкатегория", max_length=150)
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return self.nameSubcategory

    class Meta:
        db_table = 'subcategory'
        managed = True
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class QuestionsList(models.Model):
    # Вопросы и ответы #

    SIMPLE = 'SIMPLE'
    COMPLICATED = 'COMPLICATED'
    COMPLEXITY = [
        (SIMPLE, 'SIMPLE'),
        (COMPLICATED, 'COMPLICATED')
    ]

    question = models.TextField("Текст вопроса")
    answer = models.CharField("Текст ответа", max_length=150)
    clarification = models.TextField("Пояснение", blank=True, null=True)
    complexity = models.CharField("Сложность",
                              max_length=20,
                              choices=COMPLEXITY,
                              default=SIMPLE)
    subcategory = models.ForeignKey(
        Subcategory, verbose_name='Подкатегория', on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'questionsList'
        managed = True
        verbose_name = 'Список вопросов'
        verbose_name_plural = 'Список вопросов'


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

    complaint = models.TextField("Текст жалобы")
    status = models.CharField("Статус",
                              max_length=20,
                              choices=STATUS_CHOICES,
                              default=SENT)
    date = models.DateTimeField(
        "Дата", default=django.utils.timezone.now)
    question = models.ForeignKey(
        QuestionsList, verbose_name='Список вопросов', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s: %s' % (self.status, self.complaint)

    class Meta:
        db_table = 'complaints'
        managed = True
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'


class Points(models.Model):
    # Баллы #

    quantity = models.PositiveIntegerField("Количество баллов", default=0)
    user = models.OneToOneField(
        User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.quantity)

    class Meta:
        db_table = 'points'
        managed = True
        verbose_name = 'Баллы'
        verbose_name_plural = 'Баллы'


class News(models.Model):
    # Новости для блога #

    title = models.CharField("Заголовок", max_length=250)
    body = models.TextField("Текст новости")
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'
        managed = True
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    # Комментарии #

    comment = models.TextField("Текст комментария")
    date = models.DateTimeField(
        "Дата", default=django.utils.timezone.now)
    news = models.ForeignKey(
        News, verbose_name='Новости', on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.comment

    class Meta:
        db_table = 'comments'
        managed = True
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
