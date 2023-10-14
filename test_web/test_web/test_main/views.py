from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


def index(request):
    return HttpResponse('<h1>Главная</h1>')


def test_view(request):
    return HttpResponse('<h1>Страница с тестами</h1>')


def submit_answer(request):
    if request.method == 'POST':
        questions = Question.objects.all()
        for question in questions:
            # question_id = get_object_or_404(Question, id=question.id)
            answer = request.POST.get('is_correct')
            print(answer)
            print(question.is_correct)

            if answer == question.is_correct:
                # print('Well')
                messages.success(request, 'Правильный ответ.')

            else:
                print('Nope')
                messages.error(request, 'Ошибочный ответ')
                return redirect('questions_list', test_id=question.test_title_id)
    return render(request, 'test_main/submit_answer.html')


class SubjectView(ListView):
    model = Subject
    template_name = 'test_main/index.html'
    context_object_name = 'subject_list'


class TestView(ListView):
    model = Test
    template_name = 'test_main/test_view.html'
    context_object_name = 'tests'
    # slug_url_kwarg = 'test_slug'

    def get_queryset(self):
        subject = get_object_or_404(Subject, id=self.kwargs['subject_id'])
        return Test.objects.filter(test_subject=subject)


class QuestionsView(ListView):
    model = Question
    template_name = 'test_main/question_list.html'
    context_object_name = 'questions'

    def get_queryset(self):
        test_id = get_object_or_404(Test, id=self.kwargs['test_id'])
        return Question.objects.filter(test_title=test_id)
