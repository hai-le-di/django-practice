# Generated by Django 4.1.6 on 2023-02-07 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_alter_task_options_rename_datetime_task_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='task',
            new_name='name',
        ),
    ]
