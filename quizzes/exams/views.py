from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Exam, Question
from .forms import ExamForm, QuestionForm, AnswerForm


# Создание нового теста
@login_required
def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.created_by = request.user  # Связать с текущим пользователем
            exam.save()
            return redirect('add_question', exam_id=exam.id)  # Перенаправить на страницу добавления вопросов
    else:
        form = ExamForm()

    return render(request, 'exams/create_exam.html', {'form': form})


# Добавление вопросов в тест
@login_required
def add_question(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.exam = exam  # Связать вопрос с тестом
            question.order = Question.objects.filter(exam=exam).count() + 1  # Установить порядок вопроса
            question.save()
            return redirect('add_answer', question_id=question.id)  # Перенаправить на страницу добавления ответов
    else:
        question_form = QuestionForm()

    return render(request, 'exams/add_question.html', {'form': question_form, 'exam': exam})


# Добавление ответа для вопроса
@login_required
def add_answer(request, question_id):
    question = Question.objects.get(id=question_id)

    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question  # Связать ответ с вопросом
            answer.save()
            # Можно добавить логику для перехода на страницу завершения создания
            return redirect('add_answer', question_id=question.id)
    else:
        answer_form = AnswerForm()

    return render(request, 'exams/add_answer.html', {'form': answer_form, 'question': question})
