from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


def index(request):
    return HttpResponse('<h1>Главная</h1>')


def test_view(request):
    return HttpResponse('<h1>Страница с тестами</h1>')


class HomeTest(ListView):
    model = Test
    template_name = 'test_main/index.html'
    context_object_name = 'subject_list'


class TestView(DetailView):
    model = Test
    template_name = 'test_main/test_view.html'
    context_object_name = 'test'
    slug_url_kwarg = 'test_slug'


class QuestionsView(ListView):
    model = Question
    template_name = 'test_main/questions_view.html'
    context_object_name = 'questions'

