# Generated by Django 4.0.4 on 2022-04-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, default='Unknown', help_text='Name of Author to avoid Plagiarisation', max_length=20000, verbose_name='Book Author')),
                ('title', models.CharField(max_length=2000)),
                ('slug', models.SlugField(max_length=2000)),
                ('summary', models.TextField()),
                ('isbn', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('birthday', models.DateField()),
                ('author_web', models.URLField()),
            ],
        ),
    ]