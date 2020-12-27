from questionsAnswers.serializers import QuestionsDetailSerializer
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryView.as_view()),
    path('questions/', views.QuestionsListView.as_view()),
    path('questions/<int:pk>', views.QuestionsDetailView.as_view())
]
