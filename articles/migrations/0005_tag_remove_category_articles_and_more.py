# Generated by Django 5.0.3 on 2024-04-25 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_category_options_remove_article_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.RemoveField(
            model_name='category',
            name='articles',
        ),
        migrations.RemoveField(
            model_name='article',
            name='categories',
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основной тег')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article', verbose_name='Статья')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag', verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Тег статьи',
                'verbose_name_plural': 'Теги статей',
                'unique_together': {('article', 'tag')},
            },
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='articles.Scope', to='articles.tag', verbose_name='Теги'),
        ),
        migrations.DeleteModel(
            name='ArticleCategory',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
