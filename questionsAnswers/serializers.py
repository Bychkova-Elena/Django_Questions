from rest_framework import fields, serializers

from .models import QuestionsList


class QuestionsListSerializer(serializers.ModelSerializer):
    # Список вопросов #

    class Meta:
        model = QuestionsList
        fields = ("__all__")


class QuestionsBySubcatedorySerializer(serializers.ModelSerializer):
    # Список вопросов по категории #

    class Meta:
        model = QuestionsList
        exclude = ("subcategory", )
