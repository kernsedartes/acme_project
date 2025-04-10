# Generated by Django 5.1.7 on 2025-04-07 11:41

import birthday.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, help_text='Необязательное поле', max_length=20, verbose_name='Фамилия')),
                ('birthday', models.DateField(validators=[birthday.validators.real_age], verbose_name='Дата рождения')),
                ('image', models.ImageField(blank=True, upload_to='birthdays_images', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='Congratulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст поздравления')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, verbose_name='Тег')),
            ],
        ),
    ]
