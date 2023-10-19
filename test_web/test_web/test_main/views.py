from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .forms import *
import openpyxl
from .models import *
import json


def index(request):
    return HttpResponse('<h1>Главная</h1>')


def test_view(request):
    return HttpResponse('<h1>Страница с тестами</h1>')


# def submit_answer(self, request):
#     if request.method == 'POST':
#         user = User.objects.get(id=self.kwargs['user_id'])
#         question = Question.objects.get(id=self.kwargs['question_id'])
#         # questions = Question.objects.all()
#         for question in questions:
#             answer = request.POST.get('is_correct')
#             print(answer)
#             print(question.is_correct)
#
#             if answer == question.is_correct:
#                 messages.success(request, 'Правильный ответ.')
#
#             else:
#                 print('Nope')
#                 messages.error(request, 'Ошибочный ответ.')
#                 return redirect('questions_list', test_id=question.test_title_id)
#     return render(request, 'test_main/submit_answer.html')


# def answer_save(request):
#     if request.method == 'POST':
#         test_id = Test.objects.get(id='test_id')
#         print(test_id)
#         # user = User.objects.get(id=self.kwargs['user_id'])
#         # questions = Question.objects.all()
#         # for question in questions:
#         #     print(question)
#         # question = questions.filter(id=self.kwargs['question_id'])
#         # answer = Answer(user=user, question=question, selected_answer=request.POST)
#         # print(Answer.selected_answer)
#         # print(question.is_correct)
#         # answer.save()
#     return render(request, 'test_main/submit_answer.html')


# def submit_answer(request):
#     question = get_object_or_404(Question, pk=self.kwargs['question_id'])
#     selected_answer = request.POST.get('selected_answer')
#     print(question)
#     return render(request, 'test_main/submit_answer.html')


def submit_answer(request):
#     if request.method == 'POST':
#         pk = self.kwargs.get('pk')
#         user_answer = request.POST.get('is_correct')
#         question = get_object_or_404(Question, pk=pk)
#         print(user_answer)
#         # question = Question.objects.get(pk=json.loads(request.body))
#         print(question)
#         # question.user_answer = user_answer
#         # question.save()
    return render(request, 'test_main/submit_answer.html')


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_view')
    else:
        form = UserForm()
    return render(request, 'test_main/user_form.html', {'form': form})


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


class QuestionView(DetailView):
    model = Question
    template_name = 'test_main/question_view.html'
    context_object_name = 'question'
    http_method_names = ['get', 'post']

    # def post(self, request, *args, **kwargs):
    #     question = self.get_object()
    #     user_answer = request.POST.get('user_answer')
    #     question.user_answer = user_answer
    #     question.save()
    #     return render(request, 'test_main/submit_answer.html')

    def submit_answer(self, request, *args, **kwargs):
        if request.method == 'POST':
            pk = self.kwargs.get('pk')
            user_answer = request.POST.get('is_correct')
            question = get_object_or_404(Question, pk=pk)
            print(user_answer)
            question.user_answer = user_answer
            question.save()
            # question = Question.objects.get(pk=json.loads(request.body))
            print(question)
            # question.user_answer = user_answer
            # question.save()
        return render(request, 'test_main/submit_answer.html')


# class QuestionView(FormView):
#     form_class = QuestionForm
#     template_name = 'test_main/question_form.html'
#     # context_object_name = 'question'
#     # http_method_names = ['get', 'post']
#     success_url = 'test_main/question_form.html'

    # def post(self, request, *args, **kwargs):


class QuestionsView(ListView):
    model = Question
    template_name = 'test_main/question_list1.html'
    context_object_name = 'questions'

    def get_queryset(self):
        test_id = get_object_or_404(Test, id=self.kwargs['test_id'])
        return Question.objects.filter(test_title=test_id)
