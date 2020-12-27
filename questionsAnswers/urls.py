from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryView.as_view()),
    path('categories/', views.CategoriesListView.as_view()),
    path('subcategories/<int:pk>', views.SubcategoriesByCatedoryView.as_view()),
    path('questions/', views.QuestionsListView.as_view()),
    path('questions/<int:pk>', views.QuestionsBySubcatedoryView.as_view())
]
