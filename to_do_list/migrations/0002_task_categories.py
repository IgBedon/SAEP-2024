# Generated by Django 5.1.2 on 2024-11-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='categories',
            field=models.ManyToManyField(related_name='tasks', to='to_do_list.category'),
        ),
    ]
