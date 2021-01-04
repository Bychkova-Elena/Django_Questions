from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import get_object_or_404

from .models import Category, Complaint, QuestionsList, Subcategory, News
from .serializers import QuestionsListSerializer, QuestionsBySubcatedorySerializer, CategoriesListSerializer, SubcategoriesByCategorySerializer, NewsListSerializer, CommentCreateSerializer, QuestionDetailSerializer, ComplaintCreateSerializer, ComplaintsByUserSerializer, ComplaintUpdateSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class CategoriesView(View):
    # Список категорий #
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "questionsAnswers/category_list.html", {"category_list": categories})


class CategoryView(viewsets.ViewSet):

    #Вывод категорий#

    def list(self, request):
        categories = Category.objects.all()
        serializer = CategoriesListSerializer(categories, many=True)
        return Response(serializer.data)


class SubcategoryView(viewsets.ViewSet):

    #Вывод подкатегорий по категории#

    def retrieve(self, request, pk):
        subcategories = Subcategory.objects.filter(category=pk)
        serializer = SubcategoriesByCategorySerializer(
            subcategories, many=True)
        return Response(serializer.data)


class QuestionView(viewsets.ViewSet):

    #Вывод вопросов#

    def list(self, request):
        questions = QuestionsList.objects.all()
        serializer = QuestionsListSerializer(questions, many=True)
        return Response(serializer.data)

    #Вывод вопросов по подкатегории#

    def subcategoryList(self, request, pk):
        questions = QuestionsList.objects.filter(subcategory=pk)
        serializer = QuestionsBySubcatedorySerializer(questions, many=True)
        return Response(serializer.data)

    #Вывод полного вопроса#

    def retrieve(self, request, pk):
        question = QuestionsList.objects.get(pk=pk)
        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data)


class NewsView(viewsets.ViewSet):

    #Вывод новостей#

    def list(self, request):
        news = News.objects.filter(draft=False)
        serializer = NewsListSerializer(news, many=True)
        return Response(serializer.data)


class CommentView(viewsets.ViewSet):

    #Добавление комментария#

    def create(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=201)


class ComplaintView(viewsets.ViewSet):

    #Вывод жалоб пользователя#

    def retrieve(self, request, pk):
        complaints = Complaint.objects.filter(user=pk)
        serializer = ComplaintsByUserSerializer(complaints, many=True)
        return Response(serializer.data)

   #Добавление жалобы#

    def create(self, request):
        complaint = ComplaintCreateSerializer(data=request.data)
        if complaint.is_valid():
            complaint.save()
        return Response(status=201)

    #Редактирование жалобы#

    def update(self, request, pk=None):
        queryset = Complaint.objects.all()
        complaint = get_object_or_404(queryset, pk=pk)
        serializer = ComplaintUpdateSerializer(
            instance=complaint, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=201)

    #Удаление жалобы#

    def destroy(self, request, pk=None):
        complaint = Complaint.objects.get(pk=pk)
        complaint.delete()

        return Response(status=201)
