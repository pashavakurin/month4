from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list_view),
    path('post_detail/<int:id>/', views.post_detail_view),
    path('post/create', views.post_create_view),
]