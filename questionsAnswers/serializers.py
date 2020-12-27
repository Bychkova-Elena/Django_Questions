from rest_framework import fields, serializers

from .models import QuestionsList


class QuestionsListSerializer(serializers.ModelSerializer):
    # Список вопросов #

    class Meta:
        model = QuestionsList
        fields = ("question", "answer", "subcategory")


class QuestionsDetailSerializer(serializers.ModelSerializer):
    # Полный вопрос #

    subcategory = serializers.SlugRelatedField(
        slug_field="nameSubcategory", read_only=True)

    class Meta:
        model = QuestionsList
        fields = ("__all__")
