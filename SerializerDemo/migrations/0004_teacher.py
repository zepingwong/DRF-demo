# Generated by Django 4.0.4 on 2022-06-09 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SerializerDemo', '0003_rename_activate_student_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('sex', models.IntegerField(verbose_name='性别')),
                ('active', models.BooleanField(default=True, verbose_name='是否活跃')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='描述')),
            ],
        ),
    ]
