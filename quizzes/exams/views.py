from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Exam, Question, UserAnswer, Answer
from .forms import ExamForm, QuestionForm, AnswerForm


# Создание нового теста
@login_required
def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.user = request.user  # Связать с текущим пользователем
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


@login_required
def start_exam(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    questions = Question.objects.filter(exam=exam)  # Получаем все вопросы для теста

    if request.method == "POST":
        # Сохраняем ответы пользователя
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer:  # Проверяем, если пользователь ввел ответ
                UserAnswer.objects.create(
                    user=request.user,
                    exam=exam,
                    question=question,
                    user_answer=user_answer,  # Сохраняем введенный ответ
                )
        return redirect('finish_exam', exam_id=exam.id)

    return render(request, 'exams/start_exam.html', {'exam': exam, 'questions': questions})


@login_required
def finish_exam(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    user_answers = UserAnswer.objects.filter(user=request.user, exam=exam)

    correct_answers = 0
    total_questions = user_answers.count()

    # Подсчитываем количество правильных ответов
    for user_answer in user_answers:
        if (true_answer := Answer.objects.filter(question=user_answer.question).first()) and user_answer.user_answer == true_answer.text:
            correct_answers += 1

    # Вычисляем оценку
    score = round((correct_answers / total_questions) * 100, 2)  # В процентах
    user_answers.delete()
    return render(request, 'exams/finish_exam.html', {
        'exam': exam,
        'correct_answers': correct_answers,
        'total_questions': total_questions,
        'score': score,
    })
