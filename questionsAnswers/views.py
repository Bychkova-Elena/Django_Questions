from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, QuestionsList, Subcategory, News
from .serializers import QuestionsListSerializer, QuestionsBySubcatedorySerializer, CategoriesListSerializer, SubcategoriesByCategorySerializer, NewsListSerializer, CommentCreateSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


class CategoryView(View):
    # Список категорий #
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "questionsAnswers/category_list.html", {"category_list": categories})


class CategoriesListView(APIView):

    #Вывод категорий#

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoriesListSerializer(categories, many=True)
        return Response(serializer.data)


class SubcategoriesByCatedoryView(APIView):

    #Вывод подкатегорий по категории#

    def get(self, request, pk):
        subcategories = Subcategory.objects.filter(category=pk)
        serializer = SubcategoriesByCategorySerializer(
            subcategories, many=True)
        return Response(serializer.data)


class QuestionsListView(APIView):

    #Вывод вопросов#

    def get(self, request):
        questions = QuestionsList.objects.all()
        serializer = QuestionsListSerializer(questions, many=True)
        return Response(serializer.data)


class QuestionsBySubcatedoryView(APIView):

    #Вывод вопросов по подкатегории#

    def get(self, request, pk):
        questions = QuestionsList.objects.filter(subcategory=pk)
        serializer = QuestionsBySubcatedorySerializer(questions, many=True)
        return Response(serializer.data)


class NewsListView(APIView):

    #Вывод новостей#

    def get(self, request):
        news = News.objects.filter(draft=False)
        serializer = NewsListSerializer(news, many=True)
        return Response(serializer.data)


class CommentCreateView(APIView):

    #Добавление комментария#

    def post(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=201)
