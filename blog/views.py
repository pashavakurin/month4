from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import datetime
from . import models
from .constants import PAGINATION_LIMIT
from .forms import CreatePostForm
from .models import Post


def post_list_view(request):

    if request.method == 'GET':
        search_text = request.GET.get('search')
        post_value = models.Post.objects.all()
        page = int(request.GET.get('page', 1))

        max_page = post_value.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        post_value = post_value[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        if search_text:
            """ startswith, endswith, icontains """
            post_value = post_value.filter(Q(title__icontains=search_text))

        context_data = {
            'post_key': post_value,
            'user': request.user
        }

        return render(request, 'post/post.html', context=context_data)


def post_detail_view(request, id):
    if request.method == 'GET':
        post = get_object_or_404(models.Post, id=id)

        context_data = {
            'post': post,
            'hashtags': post.hashtags.all()
        }
        return render(request, 'post/post_detail.html', context=context_data)


def post_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': CreatePostForm
        }

        return render(request, 'post/create.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = CreatePostForm(data, files)

        if form.is_valid():
            cleaned_date = form.cleaned_data
            Post.objects.create(
                image=cleaned_date.get('image'),
                title=cleaned_date.get('title'),
                description=cleaned_date.get('description'),
                cost=cleaned_date.get('cost'),
                name_of_board=cleaned_date.get('name_of_board'),
                size=cleaned_date.get('size'),
            )
            return redirect('/')

        return render(request, 'post/create.html', context={'form': form})
