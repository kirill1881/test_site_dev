from django.urls import path
from .views import *

urlpatterns = [
    # path('', views.index),
    # path('test/', views.test_view),
    path('', HomeTest.as_view(), name='subject_view'),
    path('test/<slug:test_slug>/', TestView.as_view(), name='test_view'),
    # path('')
]
