# Generated by Django 4.1.6 on 2023-02-07 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('datetime', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField(auto_now=True)),
                ('done', models.BooleanField()),
                ('not_relevant_tags', models.ManyToManyField(related_name='tasks', to='list.tag')),
            ],
        ),
    ]
