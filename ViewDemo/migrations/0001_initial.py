# Generated by Django 4.0.4 on 2022-06-10 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('time_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='加入时间')),
            ],
        ),
    ]
