# Generated by Django 2.0.5 on 2018-06-05 01:09

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='分类名')),
            ],
            options={
                'verbose_name': '新闻分类',
                'verbose_name_plural': '新闻分类',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='题目')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
                ('thumbup_num', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('collects_num', models.PositiveIntegerField(default=0, verbose_name='收藏数')),
                ('comments_num', models.PositiveIntegerField(default=0, verbose_name='评论数')),
                ('clicks_num', models.PositiveIntegerField(default=0, verbose_name='点击数')),
                ('pub_date', models.DateTimeField(verbose_name='上传日期')),
                ('modify_date', models.DateTimeField(verbose_name='修改日期')),
                ('is_published', models.BooleanField(default=False, verbose_name='是否上传?')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ManyToManyField(to='news.Category', verbose_name='分类')),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
            },
        ),
    ]
