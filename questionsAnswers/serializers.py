from rest_framework import fields, serializers

from .models import QuestionsList, Category, Subcategory, News, Comment, AnswerOption, Complaint


class CategoriesListSerializer(serializers.ModelSerializer):
    # Список категорий #

    class Meta:
        model = Category
        fields = ("__all__")


class SubcategoriesByCategorySerializer(serializers.ModelSerializer):
    # Список подкатегории по категории #

    class Meta:
        model = Subcategory
        exclude = ("category", )


class QuestionsListSerializer(serializers.ModelSerializer):
    # Список вопросов #

    class Meta:
        model = QuestionsList
        fields = ("__all__")


class QuestionsBySubcatedorySerializer(serializers.ModelSerializer):
    # Список вопросов по подкатегории #

    class Meta:
        model = QuestionsList
        exclude = ("subcategory", )


class AnswerOptionSerializer(serializers.ModelSerializer):
    # Вывод вариантов ответа #

    class Meta:
        model = AnswerOption
        fields = ("first_option", "second_option",
                  "third_option", "fourth_option")


class QuestionDetailSerializer(serializers.ModelSerializer):
    # Вывод полного вопроса #

    answerOptions = AnswerOptionSerializer()

    class Meta:
        model = QuestionsList
        fields = ("__all__")


class CommentCreateSerializer(serializers.ModelSerializer):
    # Добавление комментария #

    class Meta:
        model = Comment
        exclude = ("date",)


class CommentSerializer(serializers.ModelSerializer):
    # Вывод комментариев #

    class Meta:
        model = Comment
        fields = ("comment", "date", "user")


class NewsListSerializer(serializers.ModelSerializer):
    # Список новостей #

    comments = CommentSerializer(many=True)

    class Meta:
        model = News
        exclude = ("draft", )


class ComplaintCreateSerializer(serializers.ModelSerializer):
    # Добавление жалобы #

    class Meta:
        model = Complaint
        exclude = ("date", "status")
