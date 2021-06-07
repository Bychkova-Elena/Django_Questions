import graphene
from graphene_django import DjangoObjectType

from .models import QuestionsList, Category, Subcategory, News, Comment, AnswerOption, Complaint


class CategoriesType(DjangoObjectType):
    # Список категорий #

    class Meta:
        model = Category
        fields = ("__all__")


class Query(graphene.ObjectType):

    categories = graphene.List(CategoriesType)
    def resolve_categories(self, info):
        return Category.objects.all()


schema = graphene.Schema(query=Query)
