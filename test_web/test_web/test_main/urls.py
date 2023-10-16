from django.urls import path
from .views import *
from . import views

urlpatterns = [
    # path('', views.index),
    # path('test/', views.test_view),
    path('', SubjectView.as_view(), name='subject_view'),
    path('tests/subject/<int:subject_id>/', TestView.as_view(), name='test_view'),
    path('questions/<int:test_id>', QuestionsView.as_view(), name='questions_list'),
    path('send_form/', views.submit_answer, name='submit_answer'),
    path('user_form/', user_form, name='user_form')
]
