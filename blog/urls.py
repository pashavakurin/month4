from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view),
    path('', views.post_list_view),
    path('post_detail/<int:id>/', views.post_detail_view),
]