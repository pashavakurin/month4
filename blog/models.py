from django.db import models

from blog.constants import TYPE_BOARD

class Hashtag(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Хэштег"
        verbose_name_plural = "Хэштеги"


class Post(models.Model):
    hashtags = models.ManyToManyField(Hashtag)
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='', null=True)
    description = models.TextField(blank=True, null=True)
    type_board = models.CharField(max_length=100, choices=TYPE_BOARD, null=True)
    cost = models.PositiveIntegerField(null=True)
    name_of_board = models.CharField(max_length=100, null=True)
    size = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)



    def __str__(self):
        return f' Сноуборд {self.name_of_board} ' \
               f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
