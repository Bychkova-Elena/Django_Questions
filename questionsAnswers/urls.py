from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryView.as_view()),
    path('categories/', views.CategoriesListView.as_view()),
    path('subcategories/<int:pk>', views.SubcategoriesByCatedoryView.as_view()),
    path('questions/', views.QuestionsListView.as_view()),
    path('questions/<int:pk>', views.QuestionsBySubcatedoryView.as_view()),
    path('question/<int:pk>', views.QuestionDetailView.as_view()),
    path('news/', views.NewsListView.as_view()),
    path('comment/', views.CommentCreateView.as_view()),
    path('complaint/', views.ComplaintCreateView.as_view())
]
