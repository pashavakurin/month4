# Generated by Django 4.2.6 on 2023-10-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='post',
            name='cost',
            field=models.PositiveIntegerField(null=True, verbose_name='укажите цену'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Дайте описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Загрузите фото'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name_of_board',
            field=models.CharField(max_length=100, null=True, verbose_name='укажите бренд'),
        ),
        migrations.AlterField(
            model_name='post',
            name='size',
            field=models.IntegerField(null=True, verbose_name='укажите размер'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='Название доски'),
        ),
        migrations.AlterField(
            model_name='post',
            name='type_board',
            field=models.CharField(choices=[('Boardercross', 'Boardercross'), ('Slalom', 'Slalom'), ('Half-Pipe', 'Half-Pipe'), ('Slopestyle', 'Slopestyle'), ('Freeride', 'Freeride')], max_length=100, null=True, verbose_name='Выберите тип доски'),
        ),
    ]
