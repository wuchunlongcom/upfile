# Generated by Django 2.1 on 2020-02-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Browse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer', models.CharField(blank=True, max_length=10, null=True)),
                ('mobilephone', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='org/%Y/%m', verbose_name='图片logo')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tvname', models.CharField(choices=[('爱奇艺', '爱奇艺'), ('优酷', '优酷'), ('乐视网', '乐视网'), ('腾讯视频', '腾讯视频'), ('土豆', '土豆'), ('搜狐视频', '搜狐视频'), ('56我乐', '56我乐'), ('KU6.com', 'KU6.com'), ('华数TV', '华数TV'), ('音悦Tai', '音悦Tai'), ('芒果TV', '芒果TV'), ('新浪视频', '新浪视频'), ('网易视频', '网易视频'), ('6.CN', '6.CN'), ('酷狗音乐', '酷狗音乐'), ('爆米花网', '爆米花网'), ('凤凰视频', '凤凰视频'), ('看看新闻', '看看新闻'), ('时光网', '时光网'), ('酷我音乐', '酷我音乐'), ('1905', '1905'), ('糖豆', '糖豆'), ('央视网', '央视网')], default='爱奇艺', max_length=20)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('url', models.CharField(blank=True, max_length=120, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
