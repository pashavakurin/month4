from django.shortcuts import render
from django.http import HttpResponse
import datetime

def helloView(request):
    return HttpResponse("<h1>Hello! Its my project</h1>")

def nowDate(request):
    now_date = datetime.datetime.now().replace(microsecond=0)
    return HttpResponse(f"<h1>{now_date}</h1>")

def byeView(request):
    return HttpResponse("<h1>Goodbye хаскер!</h1>")