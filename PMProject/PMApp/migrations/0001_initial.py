# Generated by Django 4.0.4 on 2022-05-24 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='the name of the Project', max_length=100)),
                ('creation_time', models.DateTimeField(auto_now_add=True, help_text='the creation time of the Project')),
                ('completion_time', models.DateTimeField(help_text='the completion time of the Project', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='the title of the task', max_length=200)),
                ('description', models.TextField(help_text='the description of the task')),
                ('time_estimate', models.IntegerField(help_text='the time estimate of the task')),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
