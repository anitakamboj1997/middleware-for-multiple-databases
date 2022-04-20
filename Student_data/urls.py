from django.urls import path
from .views import *

urlpatterns = [
    path('add/', AddStudent.as_view(),name='add'),
]
