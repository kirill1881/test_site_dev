from django.urls import path
from .views import *

urlpatterns = [
    # path('', views.index),
    # path('test/', views.test_view),
    path('', SubjectView.as_view(), name='subject_view'),
    path('test/<slug:test_slug>/', TestView.as_view(), name='test_view'),
    path('questions/<int:test_id>', QuestionsView.as_view(), name='questions_list')
]
