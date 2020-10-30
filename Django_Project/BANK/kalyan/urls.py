from django.urls import path
from .views import *

urlpattern = [
    path("all/", all.as_view()),
]