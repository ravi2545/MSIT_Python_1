from django.shortcuts import render
from django import views
# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import Dreamreal
import json


class all(views.View):
    def dis(self):
        d = {1:"prasad",2:"kalyan"}
        res = json.dumps(d)
        return JsonResponse(res)
