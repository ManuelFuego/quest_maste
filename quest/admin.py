from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('question',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ('question',)