from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import get_object_or_404

from .models import Category, Complaint, QuestionsList, Subcategory, News
from .serializers import QuestionsListSerializer, NewsCreateSerializer, QuestionsBySubcatedorySerializer, ComplaintsListSerializer, CategoriesListSerializer, SubcategoriesByCategorySerializer, NewsListSerializer, CommentCreateSerializer, QuestionDetailSerializer, ComplaintCreateSerializer, ComplaintsByUserSerializer, ComplaintUpdateSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class CategoriesView(View):

    def get(self, request):
        '''Список категорий'''

        categories = Category.objects.all()
        return render(request, "questionsAnswers/category_list.html", {"category_list": categories})


class CategoryView(viewsets.ViewSet):

    def list(self, request):
        '''Вывод категорий'''

        categories = Category.objects.all()
        serializer = CategoriesListSerializer(categories, many=True)
        return Response(serializer.data)


class SubcategoryView(viewsets.ViewSet):

    def retrieve(self, request, pk):
        '''Вывод подкатегорий категории'''

        subcategories = Subcategory.objects.filter(category=pk)
        serializer = SubcategoriesByCategorySerializer(
            subcategories, many=True)
        return Response(serializer.data)


class QuestionView(viewsets.ViewSet):

    def list(self, request):
        '''Вывод вопросов'''

        questions = QuestionsList.objects.all()
        serializer = QuestionsListSerializer(questions, many=True)
        return Response(serializer.data)

    def subcategoryList(self, request, pk):
        '''Вывод вопросов подкатегории'''

        questions = QuestionsList.objects.filter(subcategory=pk)
        serializer = QuestionsBySubcatedorySerializer(questions, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        '''Вывод вопроса'''

        question = QuestionsList.objects.get(pk=pk)
        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data)


class NewsView(viewsets.ViewSet):

    def list(self, request):
        '''Вывод новостей'''

        news = News.objects.filter(draft=False)
        serializer = NewsListSerializer(news, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        '''Добавление новости'''
          
        news = NewsCreateSerializer(data=request.data)
        if news.is_valid():
            news.save()
        return Response(status=201)

    def update(self, request, pk=None):
        '''Редактирование новости'''

        queryset = News.objects.all()
        news = get_object_or_404(queryset, pk=pk)
        serializer = NewsCreateSerializer(
            instance=news, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=201)

    def destroy(self, request, pk=None):
        '''Удаление новости'''

        news = News.objects.get(pk=pk)
        news.delete()

        return Response(status=201)

class CommentView(viewsets.ViewSet):

    def create(self, request):
        '''Добавление комментария'''

        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=201)


class ComplaintView(viewsets.ViewSet):

    def list(self, request):
        '''Вывод жалоб'''

        complaints = Complaint.objects.all()
        serializer = ComplaintsListSerializer(complaints, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        '''Вывод жалоб пользователя'''

        complaints = Complaint.objects.filter(user=pk)
        serializer = ComplaintsByUserSerializer(complaints, many=True)
        return Response(serializer.data)

    def create(self, request):
        '''Добавление жалобы'''

        complaint = ComplaintCreateSerializer(data=request.data)
        if complaint.is_valid():
            complaint.save()
        return Response(status=201)

    def update(self, request, pk=None):
        '''Редактирование жалобы'''

        queryset = Complaint.objects.all()
        complaint = get_object_or_404(queryset, pk=pk)
        serializer = ComplaintUpdateSerializer(
            instance=complaint, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=201)

    def destroy(self, request, pk=None):
        '''Удаление жалобы'''

        complaint = Complaint.objects.get(pk=pk)
        complaint.delete()

        return Response(status=201)
