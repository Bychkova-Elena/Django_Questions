from rest_framework import fields, serializers

from .models import QuestionsList, Category, Subcategory


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
