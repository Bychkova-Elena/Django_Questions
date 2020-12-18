from django.contrib import admin
from .models import Category, Subcategory, QuestionsList, AnswerOption, Complaint, Points, TopPlayer, News, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("nameCategory", )
    list_display_links = ("nameCategory",)
    search_fields = ("nameCategory", )


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("nameSubcategory", "category")
    list_display_links = ("nameSubcategory",)
    list_filter = ("category",)
    search_fields = ("nameSubcategory", "category__nameCategory")


@admin.register(QuestionsList)
class QuestionsListAdmin(admin.ModelAdmin):
    list_display = ("question", "answer", "clarification",
                    "subcategory")
    list_display_links = ("question",)
    list_filter = ("subcategory",)
    search_fields = ("question", "answer", "subcategory__nameSubcategory")


@admin.register(AnswerOption)
class AnswerOptionAdmin(admin.ModelAdmin):
    list_display = ("question",  "first_option", "second_option", "third_option",
                    "fourth_option")
    list_display_links = ("question",)
    search_fields = ("question__question", )


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("status",  "complaint", "question", "user")
    list_display_links = ("complaint",)
    list_filter = ("status",)
    search_fields = ("status", "complaint", "question", "user")
    readonly_fields = ("complaint", "question", "user")


@admin.register(Points)
class PointsAdmin(admin.ModelAdmin):
    list_display = ("user",  "quantity", "numberGames", "commonPoints")
    list_display_links = ("user",)
    search_fields = ("user__username",)


@admin.register(TopPlayer)
class TopPlayerAdmin(admin.ModelAdmin):
    list_display = ("user", )
    list_display_links = ("user",)
    search_fields = ("user__username",)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title",  "body")
    list_display_links = ("title",)
    search_fields = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user",  "comment", "news")
    list_display_links = ("comment",)
    search_fields = ("news__title", "comment", "user__username")
    readonly_fields = ("comment", "news", "user")
