from rest_framework import fields, serializers

from .models import QuestionsList, Category, Subcategory, News, Comment, Complaint


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



class QuestionDetailSerializer(serializers.ModelSerializer):
    # Вывод полного вопроса #

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

class NewsCreateSerializer(serializers.ModelSerializer):
    # Добавление новости #

    class Meta:
        model = News
        exclude = ("draft",)


class ComplaintCreateSerializer(serializers.ModelSerializer):
    # Добавление жалобы #

    class Meta:
        model = Complaint
        exclude = ("date", "status")

class ComplaintsListSerializer(serializers.ModelSerializer):
    # Список жалоб #

    class Meta:
        model = Complaint
        fields = ("__all__")


class ComplaintsByUserSerializer(serializers.ModelSerializer):
    # Список жалоб пользователя #

    class Meta:
        model = Complaint
        exclude = ("user", )


class ComplaintUpdateSerializer(serializers.ModelSerializer):
    # Редактирование жалобы #

    class Meta:
        model = Complaint
        fields = ("complaint", "question", "date")
