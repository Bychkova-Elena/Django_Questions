from django.contrib import admin
from .models import Category, Subcategory, Question, Answer, AnswerOption, Complaint, Point, TopPlayer, News

# Register your models here.

admin.site.register(Category, Subcategory, Question, Answer,
                    AnswerOption, Complaint, Point, TopPlayer, News)
