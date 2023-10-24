from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from . import models


def postListView(request):
    post_value = models.Post.objects.all()
    html_file_name = 'post/post.html'
    context = {
        'post_key': post_value,
    }
    return render(request, html_file_name, context)

def postDetailView(request, id):
    post_id = get_object_or_404(models.Post, id=id)
    return render(request, 'post/post_detail.html', {'post_id': post_id})

def helloView(request):
    return HttpResponse("<h1>Hello! Its my project</h1>")

def nowDate(request):
    now_date = datetime.datetime.now().replace(microsecond=0)
    return HttpResponse(f"<h1>{now_date}</h1>")

def byeView(request):
    return HttpResponse("<h1>Goodbye хаскер!</h1>")
