# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
from django.conf import settings
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='username', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True)),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=254)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('avatar', models.ImageField(verbose_name='用户头像', default='avatar/default.png', blank=True, null=True, max_length=200, upload_to='avatar/%Y/%m')),
                ('qq', models.CharField(verbose_name='QQ号码', null=True, blank=True, max_length=20)),
                ('mobile', models.CharField(verbose_name='手机号码', null=True, unique=True, blank=True, max_length=11)),
                ('url', models.URLField(verbose_name='个人网页地址', null=True, blank=True, max_length=100)),
                ('groups', models.ManyToManyField(related_name='user_set', verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', to='auth.Permission', related_query_name='user')),
            ],
            options={
                'verbose_name': '用户',
                'ordering': ['-id'],
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='广告标题', max_length=50)),
                ('description', models.CharField(verbose_name='广告描述', max_length=200)),
                ('image_url', models.ImageField(verbose_name='图片路径', upload_to='ad/%Y/%m')),
                ('callback_url', models.URLField(verbose_name='回调url', null=True, blank=True)),
                ('date_publish', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
                ('index', models.IntegerField(verbose_name='排列顺序(从小到大)', default=999)),
            ],
            options={
                'verbose_name': '广告',
                'ordering': ['index', 'id'],
                'verbose_name_plural': '广告',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='文章标题', max_length=50)),
                ('desc', models.CharField(verbose_name='文章描述', max_length=50)),
                ('content', models.TextField(verbose_name='文章内容')),
                ('click_count', models.IntegerField(verbose_name='点击次数', default=0)),
                ('is_recommend', models.BooleanField(verbose_name='是否推荐', default=False)),
                ('date_publish', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
            ],
            options={
                'verbose_name': '文章',
                'ordering': ['-date_publish'],
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='分类名称', max_length=30)),
                ('index', models.IntegerField(verbose_name='显示顺序(从小到大)', default=999)),
            ],
            options={
                'verbose_name': '分类',
                'ordering': ['index', 'id'],
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='评论内容')),
                ('username', models.CharField(verbose_name='用户名', null=True, blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='邮箱地址', null=True, blank=True, max_length=50)),
                ('url', models.URLField(verbose_name='个人网页地址', null=True, blank=True, max_length=100)),
                ('date_publish', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
                ('article', models.ForeignKey(related_name='entries', verbose_name='文章', blank=True, to='blog.Article', null=True)),
                ('pid', models.ForeignKey(verbose_name='父级评论', blank=True, to='blog.Comment', null=True)),
                ('user', models.ForeignKey(verbose_name='用户', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '评论',
                'ordering': ['-date_publish'],
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='标题', max_length=50)),
                ('description', models.CharField(verbose_name='友情链接描述', max_length=200)),
                ('callback_url', models.URLField(verbose_name='url地址')),
                ('date_publish', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
                ('index', models.IntegerField(verbose_name='排列顺序(从小到大)', default=999)),
            ],
            options={
                'verbose_name': '友情链接',
                'ordering': ['index', 'id'],
                'verbose_name_plural': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='标签名称', max_length=30)),
            ],
            options={
                'verbose_name': '标签',
                'ordering': ['id'],
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='分类', blank=True, to='blog.Category', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
