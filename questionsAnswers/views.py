from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, QuestionsList
from .serializers import QuestionsListSerializer, QuestionsDetailSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


class CategoryView(View):
    # Список категорий #
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "questionsAnswers/category_list.html", {"category_list": categories})


class QuestionsListView(APIView):

    #Вывод вопросов#

    def get(self, request):
        questions = QuestionsList.objects.all()
        serializer = QuestionsListSerializer(questions, many=True)
        return Response(serializer.data)


class QuestionsDetailView(APIView):

    #Вывод вопроса#

    def get(self, request, pk):
        question = QuestionsList.objects.get(id=pk)
        serializer = QuestionsDetailSerializer(question)
        return Response(serializer.data)
