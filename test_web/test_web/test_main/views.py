from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


def index(request):
    return HttpResponse('<h1>Главная</h1>')


def test_view(request):
    return HttpResponse('<h1>Страница с тестами</h1>')


class SubjectView(ListView):
    model = Subject
    template_name = 'test_main/index.html'
    context_object_name = 'subject_list'


class TestView(DetailView):
    model = Test
    template_name = 'test_main/test_view.html'
    context_object_name = 'test'
    slug_url_kwarg = 'test_slug'

    def get_queryset(self):
        test_slug = self.kwargs['test_slug']
        return Test.objects.filter(slug=test_slug)


class QuestionsView(ListView):
    model = Question
    template_name = 'test_main/question_list.html'
    context_object_name = 'questions'

    def get_queryset(self):
        # question_id = self.kwargs['pk']
        return Question.objects.all().select_related('test_title')
