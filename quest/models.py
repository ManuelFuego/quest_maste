import uuid
from django.contrib import admin
from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=250, db_index=True)
    question_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    weight = models.FloatField(default=1)

    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return str(self.question)


class Answer(models.Model):
    question = models.ForeignKey(Question, max_length=250, on_delete=models.CASCADE, related_name='answer')
    answer = models.CharField(max_length=250)
    answer_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    is_right = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return f' {str(self.question)} {str(self.answer)} {str(self.is_right)}'


class QuestionsInline(admin.TabularInline):
    model = Answer


# @admin.register(Question)
class quest_admin(admin.ModelAdmin):
    inlines = [QuestionsInline]


# @admin.register(Answer)
class answer_result(admin.ModelAdmin):
    list_display = ("question", "answer", "is_right")
