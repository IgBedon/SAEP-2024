# Generated by Django 5.1.2 on 2024-11-21 13:13

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0004_environment_collaborators'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='environment',
        ),
        migrations.RemoveField(
            model_name='task',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='collaborators',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='task',
            name='environment',
        ),
        migrations.RemoveField(
            model_name='task',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='task',
            name='title',
        ),
        migrations.AddField(
            model_name='task',
            name='department_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='register_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='A Fazer', max_length=50),
        ),
        migrations.DeleteModel(
            name='Attachment',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Environment',
        ),
    ]