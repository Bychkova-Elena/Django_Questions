import graphene
from graphene_django import DjangoObjectType

from .models import QuestionsList, Category, Subcategory, News, Comment, AnswerOption, Complaint


class CategoriesType(DjangoObjectType):
    # Список категорий #

    class Meta:
        model = Category
        fields = ("__all__")


class Query(graphene.ObjectType):

    all_categories = graphene.List(CategoriesType)


schema = graphene.Schema(query=Query)
