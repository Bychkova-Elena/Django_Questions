from django.contrib import admin
from .models import Category, Subcategory, QuestionsList, AnswerOption, Complaint, Points, TopPlayer, News, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(QuestionsList)
admin.site.register(AnswerOption)
admin.site.register(Complaint)
admin.site.register(Points)
admin.site.register(TopPlayer)
admin.site.register(News)
admin.site.register(Comment)
