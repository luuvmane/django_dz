# Generated by Django 5.0.6 on 2024-06-23 20:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название продукта')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание продукта')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Фото продукта')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Цена продукта')),
                ('created_at', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateField(blank=True, null=True, verbose_name='Дата изменения')),
                ('manufactured_at', models.DateField(blank=True, null=True, verbose_name='Дата изготовления')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Products', to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
