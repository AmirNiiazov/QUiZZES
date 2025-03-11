from django import forms
from .models import Exam, Question, Answer


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'description']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
