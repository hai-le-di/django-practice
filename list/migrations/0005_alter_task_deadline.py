# Generated by Django 4.1.6 on 2023-02-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_rename_task_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]