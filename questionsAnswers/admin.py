from django.contrib import admin
from .models import Category, Subcategory, QuestionsList, AnswerOption, Complaint, Points, TopPlayer, News, Comment, User
from django import forms


from ckeditor_uploader.widgets import CKEditorUploadingWidget
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ExportActionMixin


class NewsAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


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


class PointsInline(admin.StackedInline):
    model = Points


class UserResource(resources.ModelResource):

    class Meta:
        model = User


@admin.register(User)
class UserAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = UserResource
    search_fields = ("username", )
    inlines = [PointsInline]
    save_on_top = True


class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category


@admin.register(Category)
class CategoryAdmin(ImportExportActionModelAdmin):
    resource_class = CategoryResource
    list_display = ("nameCategory", )
    list_display_links = ("nameCategory",)
    search_fields = ("nameCategory", )
    inlines = [SubcategoryInline]
    save_on_top = True
    save_as = True


class SubcategoryResource(resources.ModelResource):
    category = fields.Field(column_name="category", attribute="category",
                            widget=ForeignKeyWidget(Category, "nameCategory"))

    class Meta:
        model = Subcategory


@admin.register(Subcategory)
class SubcategoryAdmin(ImportExportActionModelAdmin):
    resource_class = SubcategoryResource
    list_display = ("nameSubcategory", "category")
    list_display_links = ("nameSubcategory",)
    list_filter = ("category",)
    search_fields = ("nameSubcategory", "category__nameCategory")
    inlines = [QuestionsListInline]
    save_on_top = True
    save_as = True


class QuestionsListResource(resources.ModelResource):
    subcategory = fields.Field(column_name="subcategory", attribute="subcategory",
                               widget=ForeignKeyWidget(Subcategory, "nameSubcategory"))

    class Meta:
        model = QuestionsList


@admin.register(QuestionsList)
class QuestionsListAdmin(ImportExportActionModelAdmin):
    resource_class = QuestionsListResource
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
        ("Пояснение", {
            "classes": ("collapse", ),
            "fields": (("clarification"),)
        }),
        (None, {
            "fields": (("subcategory"),)
        }),
    )


class AnswerOptionResource(resources.ModelResource):

    class Meta:
        model = AnswerOption


@admin.register(AnswerOption)
class AnswerOptionAdmin(ImportExportActionModelAdmin):
    resource_class = AnswerOptionResource
    list_display = ("question", "first_option", "second_option", "third_option",
                    "fourth_option")
    list_display_links = ("question",)
    search_fields = ("question__question", )
    save_as = True
    fieldsets = (
        (None, {
            "fields": (("first_option", "second_option", "third_option", "fourth_option"),)
        }),
        ("Текст вопроса", {
            "classes": ("collapse", ),
            "fields": (("question"),)
        }),
    )


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("status",  "complaint", "date", "user")
    list_display_links = ("complaint",)
    list_filter = ("status",)
    actions = ["changeOnUnderConsideration",
               "changeOnREJECT", "changeOnACCEPT", "changeOnFIXED"]
    search_fields = ("status", "complaint", "question", "user")
    readonly_fields = ("complaint", "question", "date", "user")

    def changeOnUnderConsideration(self, request, queryset):
        #Изменить статус на под рассмотрением#
        row_update = queryset.update(status='UNDER CONSIDERATION')
        if row_update == 1:
            message_bit = "The status of 1 entry has been changed"
        else:
            message_bit = f"The status of {row_update} entries has been changed"
        self.message_user(request, f"{message_bit}")

    def changeOnREJECT(self, request, queryset):
        #Изменить статус на отклонено#
        row_update = queryset.update(status='REJECT')
        if row_update == 1:
            message_bit = "The status of 1 entry has been changed"
        else:
            message_bit = f"The status of {row_update} entries has been changed"
        self.message_user(request, f"{message_bit}")

    def changeOnACCEPT(self, request, queryset):
        #Изменить статус на принято в работу#
        row_update = queryset.update(status='ACCEPT')
        if row_update == 1:
            message_bit = "The status of 1 entry has been changed"
        else:
            message_bit = f"The status of {row_update} entries has been changed"
        self.message_user(request, f"{message_bit}")

    def changeOnFIXED(self, request, queryset):
        #Изменить статус на исправлено#
        row_update = queryset.update(status='FIXED')
        if row_update == 1:
            message_bit = "The status of 1 entry has been changed"
        else:
            message_bit = f"The status of {row_update} entries has been changed"
        self.message_user(request, f"{message_bit}")

    changeOnUnderConsideration.short_description = "Take for consideration"
    changeOnUnderConsideration.allowed_permissions = ('change', )

    changeOnREJECT.short_description = "Reject"
    changeOnREJECT.allowed_permissions = ('change', )

    changeOnACCEPT.short_description = "Take to work"
    changeOnACCEPT.allowed_permissions = ('change', )

    changeOnFIXED.short_description = "Set status - fixed"
    changeOnFIXED.allowed_permissions = ('change', )


class PointsResource(resources.ModelResource):
    user = fields.Field(column_name="user", attribute="user",
                        widget=ForeignKeyWidget(User, "username"))

    class Meta:
        model = Points


@admin.register(Points)
class PointsAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = PointsResource
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


class TopPlayerResource(resources.ModelResource):
    user = fields.Field(column_name="user", attribute="user",
                        widget=ForeignKeyWidget(User, "username"))

    class Meta:
        model = TopPlayer


@admin.register(TopPlayer)
class TopPlayerAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = TopPlayerResource
    list_display = ("user", )
    list_display_links = ("user",)
    search_fields = ("user__username",)


class NewsResource(resources.ModelResource):

    class Meta:
        model = News


@admin.register(News)
class NewsAdmin(ImportExportActionModelAdmin):
    resource_class = NewsResource
    list_display = ("title", "draft")
    list_filter = ("draft", )
    list_editable = ("draft",)
    list_display_links = ("title",)
    search_fields = ("title",)
    actions = ["publish", "unpublish"]
    form = NewsAdminForm
    inlines = [CommentInline]
    save_on_top = True

    def unpublish(self, request, queryset):
        #Снять с публикации#
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 record was changed"
        else:
            message_bit = f"{row_update} records were changed"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        #Опубликовать#
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 record was changed"
        else:
            message_bit = f"{row_update} records were changed"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Publish"
    publish.allowed_permissions = ('change', )

    unpublish.short_description = "Unpublish"
    unpublish.allowed_permissions = ('change',)


class CommentResource(resources.ModelResource):
    user = fields.Field(column_name="user", attribute="user",
                        widget=ForeignKeyWidget(User, "username"))

    class Meta:
        model = Comment


@admin.register(Comment)
class CommentAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = CommentResource
    list_display = ("comment", "date", "user")
    list_display_links = ("comment",)
    search_fields = ("comment", "user__username")
    readonly_fields = ("comment", "news", "date", "user")
