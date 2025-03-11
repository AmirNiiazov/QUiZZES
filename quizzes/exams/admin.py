from django.contrib import admin
from .models import Exam, Question, Answer, Result


@admin.register(Exam)
class ExamsAdmin(admin.ModelAdmin):
    ordering = ['-id']


@admin.register(Question)
class QuestionsAdmin(admin.ModelAdmin):
    ordering = ['-id']


@admin.register(Answer)
class AnswersAdmin(admin.ModelAdmin):
    ordering = ['-id']


@admin.register(Result)
class ResultsAdmin(admin.ModelAdmin):
    ordering = ['-id']
