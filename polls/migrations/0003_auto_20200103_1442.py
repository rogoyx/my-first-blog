# Generated by Django 2.2.7 on 2020-01-03 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='blog.Post'),
        ),
    ]
