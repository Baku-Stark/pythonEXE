# Generated by Django 4.1.6 on 2023-02-10 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='user_ID',
            new_name='user',
        ),
    ]
