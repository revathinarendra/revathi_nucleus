# Generated by Django 4.2.4 on 2024-04-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0002_user_performance_doubt_ques_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_performance',
            name='doubt_ques',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_performance',
            name='important_ques',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_performance',
            name='star_ques',
            field=models.TextField(blank=True, null=True),
        ),
    ]
