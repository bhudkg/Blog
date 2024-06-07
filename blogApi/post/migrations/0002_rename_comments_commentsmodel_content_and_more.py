# Generated by Django 5.0.6 on 2024-06-07 03:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentsmodel',
            old_name='comments',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='commentsmodel',
            name='uploaded_at',
        ),
        migrations.AlterField(
            model_name='commentsmodel',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.postmodel'),
            preserve_default=False,
        ),
    ]
