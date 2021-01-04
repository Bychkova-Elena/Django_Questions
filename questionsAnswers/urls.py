from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoriesView.as_view()),
    path('categories/', views.CategoryView.as_view({'get': 'list'})),
    path('subcategories/<int:pk>/',
         views.SubcategoryView.as_view({'get': 'retrieve'})),
    path('questions/', views.QuestionView.as_view({'get': 'list'})),
    path('questions/<int:pk>/',
         views.QuestionView.as_view({'get': 'subcategoryList'})),
    path('question/<int:pk>/',
         views.QuestionView.as_view({'get': 'retrieve'})),
    path('news/', views.NewsView.as_view({'get': 'list'})),
    path('comment-create/', views.CommentView.as_view({'post': 'create'})),
    path('complaint-create/', views.ComplaintView.as_view({'post': 'create'})),
    path('complaints/<int:pk>',
         views.ComplaintView.as_view({'get': 'retrieve'})),
    path('complaint-update/<int:pk>',
         views.ComplaintView.as_view({'put': 'update'})),

    path('complaint-delete/<int:pk>',
         views.ComplaintView.as_view({'delete': 'destroy'})),
]
