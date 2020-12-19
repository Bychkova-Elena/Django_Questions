from django.contrib import admin
from .models import Category, Subcategory, QuestionsList, AnswerOption, Complaint, Points, TopPlayer, News, Comment


class ComplaintInline(admin.StackedInline):
    model = Complaint
    extra = 0
    readonly_fields = ("complaint", "user", "date")


class AnswerOptionInline(admin.StackedInline):
    model = AnswerOption


class SubcategoryInline(admin.StackedInline):
    model = Subcategory


class QuestionsListInline(admin.StackedInline):
    model = QuestionsList


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    readonly_fields = ("comment", "user", "date")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("nameCategory", )
    list_display_links = ("nameCategory",)
    search_fields = ("nameCategory", )
    inlines = [SubcategoryInline]
    save_on_top = True
    save_as = True


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("nameSubcategory", "category")
    list_display_links = ("nameSubcategory",)
    list_filter = ("category",)
    search_fields = ("nameSubcategory", "category__nameCategory")
    inlines = [QuestionsListInline]
    save_on_top = True
    save_as = True


@admin.register(QuestionsList)
class QuestionsListAdmin(admin.ModelAdmin):
    list_display = ("question", "answer", "subcategory")
    list_display_links = ("question",)
    list_filter = ("subcategory",)
    search_fields = ("question", "answer", "subcategory__nameSubcategory")
    inlines = [ComplaintInline, AnswerOptionInline]
    save_on_top = True
    save_as = True
    fieldsets = (
        (None, {
            "fields": (("question", "answer"),)
        }),
        ("Clarification", {
            "classes": ("collapse", ),
            "fields": (("clarification"),)
        }),
        (None, {
            "fields": (("subcategory"),)
        }),
    )


@admin.register(AnswerOption)
class AnswerOptionAdmin(admin.ModelAdmin):
    list_display = ("question", "first_option", "second_option", "third_option",
                    "fourth_option")
    list_display_links = ("question",)
    search_fields = ("question__question", )
    save_as = True
    fieldsets = (
        (None, {
            "fields": (("first_option", "second_option", "third_option", "fourth_option"),)
        }),
        ("Question", {
            "classes": ("collapse", ),
            "fields": (("question"),)
        }),
    )


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("status",  "complaint", "date", "user")
    list_display_links = ("complaint",)
    list_filter = ("status",)
    search_fields = ("status", "complaint", "question", "user")
    readonly_fields = ("complaint", "question", "date", "user")


@admin.register(Points)
class PointsAdmin(admin.ModelAdmin):
    list_display = ("user",  "quantity", "numberGames", "commonPoints")
    list_display_links = ("user",)
    readonly_fields = ("user", )
    search_fields = ("user__username",)
    fieldsets = (
        (None, {
            "fields": (("user"),)
        }),
        (None, {
            "fields": (("quantity", "numberGames", "commonPoints"),)
        }),
    )


@admin.register(TopPlayer)
class TopPlayerAdmin(admin.ModelAdmin):
    list_display = ("user", )
    list_display_links = ("user",)
    search_fields = ("user__username",)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", )
    list_display_links = ("title",)
    search_fields = ("title",)
    inlines = [CommentInline]
    save_on_top = True


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment", "date", "user")
    list_display_links = ("comment",)
    search_fields = ("comment", "user__username")
    readonly_fields = ("comment", "news", "date", "user")
