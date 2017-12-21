# Generated by Django 2.0 on 2017-12-21 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UPortalApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='place_of_publication',
            options={'verbose_name': 'Место публикации', 'verbose_name_plural': 'Места публикации'},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.AlterField(
            model_name='author',
            name='nameEng',
            field=models.CharField(max_length=200, verbose_name='full name in english'),
        ),
        migrations.AlterField(
            model_name='author',
            name='nameRus',
            field=models.CharField(max_length=200, verbose_name='ФИО на русском'),
        ),
        migrations.AlterField(
            model_name='files_of_publication',
            name='file',
            field=models.FileField(upload_to='', verbose_name='Файлы публикации'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date_of_publication',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=models.TextField(verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='language_of_publication',
            field=models.CharField(max_length=255, verbose_name='Язык публикации'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='links',
            field=models.TextField(verbose_name='Список ссылок'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='pages',
            field=models.CharField(max_length=255, verbose_name='Страницы публикации (с X по Y)'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='place_of_publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UPortalApp.Place_of_publication'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='type_of_index',
            field=models.CharField(max_length=255, verbose_name='Типы индексации'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='type_of_publication',
            field=models.CharField(max_length=255, verbose_name='f)\tТип публикации '),
        ),
    ]