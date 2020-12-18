from django.shortcuts import render
from django.views.generic.base import View

from .models import Category


class CategoryView(View):
    # Список категорий #
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "questionsAnswers/category_list.html", {"category_list": categories})
