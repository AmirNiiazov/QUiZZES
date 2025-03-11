from django.db import models
from django.contrib.auth.models import User


class Exam(models.Model):
    title = models.CharField(max_length=200)  # Название теста
    description = models.TextField()  # Описание теста
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор теста (ссылка на пользователя)

    def __str__(self):
        return self.title


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')  # Ссылка на тест
    text = models.TextField()  # Текст вопроса
    order = models.PositiveIntegerField()  # Порядок вопроса в тесте

    class Meta:
        ordering = ['order']  # Сортировка вопросов по порядку

    def __str__(self):
        return f"Вопрос {self.order}: {self.text[:50]}..."  # Краткое представление


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')  # Ссылка на вопрос
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Результат для {self.user.username} - {self.score} баллов"
