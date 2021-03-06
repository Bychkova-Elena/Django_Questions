from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoriesView.as_view()),
    path('categories/', views.CategoryView.as_view({'get': 'list'})),
    path('categories/<int:pk>/subcategories/',
         views.SubcategoryView.as_view({'get': 'retrieve'})),
    path('questions/', views.QuestionView.as_view({'get': 'list'})),
    path('subcategories/<int:pk>/questions/',
         views.QuestionView.as_view({'get': 'subcategoryList'})),
    path('questions/<int:pk>/',
         views.QuestionView.as_view({'get': 'retrieve'})),
    path('news/', views.NewsView.as_view({'get': 'list'})),
    path('comments/create/', views.CommentView.as_view({'post': 'create'})),
    path('complaints/create/',
         views.ComplaintView.as_view({'post': 'create'})),
    path('users/<int:pk>/complaints/',
         views.ComplaintView.as_view({'get': 'retrieve'})),
    path('complaints/update/<int:pk>',
         views.ComplaintView.as_view({'put': 'update'})),

    path('complaints/delete/<int:pk>',
         views.ComplaintView.as_view({'delete': 'destroy'})),
]
