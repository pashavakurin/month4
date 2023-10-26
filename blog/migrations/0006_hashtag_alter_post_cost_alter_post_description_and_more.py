# Generated by Django 4.2.6 on 2023-10-26 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_options_alter_post_cost_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Хэштег',
                'verbose_name_plural': 'Хэштеги',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='cost',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='name_of_board',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='size',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='type_board',
            field=models.CharField(choices=[('Boardercross', 'Boardercross'), ('Slalom', 'Slalom'), ('Half-Pipe', 'Half-Pipe'), ('Slopestyle', 'Slopestyle'), ('Freeride', 'Freeride')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hashtags',
            field=models.ManyToManyField(to='blog.hashtag'),
        ),
    ]