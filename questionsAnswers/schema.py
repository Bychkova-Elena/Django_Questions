import graphene
from graphene_django import DjangoObjectType

from .models import QuestionsList, Category, Subcategory, News, Comment, Complaint


class CategoriesType(DjangoObjectType):
    # Список категорий #

    class Meta:
        model = Category
        fields = ("__all__")


class SubcategoriesType(DjangoObjectType):
    # Список подкатегорий #

    class Meta:
        model = Subcategory
        fields = ("__all__")

class QuestionsType(DjangoObjectType):
    # Список вопросов #

    class Meta:
        model = QuestionsList
        fields = ("__all__")

class NewsType(DjangoObjectType):
    # Список новостей #

    class Meta:
        model = News
        fields = ("__all__")


class CreateNews(graphene.Mutation):
  class Arguments:
    title = graphene.String()
    body = graphene.String()
  news = graphene.Field(NewsType)

  def mutate(self, info, title, body):
    news = News.objects.create(
      title = title,
      body = body
    )

    news.save()

    return CreateNews(
      news=news
    )

class UpdateNews(graphene.Mutation):
  
  class Arguments:
    id = graphene.ID()
    title = graphene.String()
    body = graphene.String()
  news = graphene.Field(NewsType)

  def mutate(self, info, id, title=None, body=None):
    news = News.objects.get(pk=id)
    news.title = title if title is not None else news.title
    news.body = body if body is not None else news.body

    news.save()
    
    return UpdateNews(news=news)


class DeleteNews(graphene.Mutation):
  class Arguments:
   
    id = graphene.ID()

  news = graphene.Field(NewsType)

  def mutate(self, info, id):
    news = News.objects.get(pk=id)
    if news is not None:
      news.delete()
    return DeleteNews(news=news)


class Query(graphene.ObjectType):

    categories = graphene.List(CategoriesType)
    def resolve_categories(self, info):
        return Category.objects.all()

    subcategories = graphene.List(SubcategoriesType, id=graphene.ID())
    def resolve_subcategories(self, info, id):
        return Subcategory.objects.filter(category_id=id)

    questions = graphene.List(QuestionsType, id=graphene.ID())
    def resolve_questions(self, info, id):
        return QuestionsList.objects.filter(subcategory_id=id)

    news = graphene.List(NewsType)
    def resolve_news(self, info):
        return News.objects.all()


class Mutation(graphene.ObjectType):
  create_news = CreateNews.Field()
  update_news = UpdateNews.Field()
  delete_news = DeleteNews.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
