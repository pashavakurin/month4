from django.db import models

class Post(models.Model):

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    TYPE_BOARD = (
        ('Boardercross', 'Boardercross'),
        ('Slalom', 'Slalom'),
        ('Half-Pipe', 'Half-Pipe'),
        ('Slopestyle', 'Slopestyle'),
        ('Freeride', 'Freeride')
    )

    title = models.CharField(max_length=100, verbose_name='Название доски', null=True)
    image = models.ImageField(upload_to='', verbose_name='Загрузите фото', null=True)
    description = models.TextField(blank=True, null=True, verbose_name='Дайте описание')
    type_board = models.CharField(max_length=100, choices=TYPE_BOARD, verbose_name='Выберите тип доски', null=True)
    cost = models.PositiveIntegerField(verbose_name='укажите цену', null=True)
    name_of_board = models.CharField(max_length=100, verbose_name='укажите бренд', null=True)
    size = models.IntegerField(null=True, verbose_name='укажите размер')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f' Сноуборд {self.name_of_board} ' \
               f'{self.title}'
