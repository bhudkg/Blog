# Generated by Django 5.0.6 on 2024-06-07 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_rename_comments_commentsmodel_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='slug',
        ),
    ]
