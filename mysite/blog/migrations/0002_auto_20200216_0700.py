# Generated by Django 2.2.6 on 2020-02-15 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='image/', verbose_name='图片logo'),
        ),
    ]
