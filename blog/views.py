from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from . import models


def post_list_view(request):
    if request.method == 'GET':
        post_value = models.Post.objects.all()

        context_data = {
            'post_key': post_value
        }

        return render(request, 'post/post.html', context=context_data)

def post_detail_view(request, id):
    if request.method == 'GET':
        post_id = get_object_or_404(models.Post, id=id)

        context_data = {
            'post_id': post_id,
            'hashtags': post_id.hashtags.all()
        }
        return render(request, 'post/post_detail.html',context=context_data)

def hello_view(request):
    return HttpResponse("<h1>Hello! Its my project</h1>")
