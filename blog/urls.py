from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.helloView),
    path('now_date/', views.nowDate),
    path('bye/', views.byeView),
    path('', views.postListView),
]