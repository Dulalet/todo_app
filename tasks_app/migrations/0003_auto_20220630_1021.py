# Generated by Django 3.1.5 on 2022-06-30 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0002_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='priority',
        ),
        migrations.AddField(
            model_name='task',
            name='executed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]