# Generated by Django 4.2.3 on 2023-10-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('1', 'Один ответ'), ('2', 'Много ответов'), ('3', 'Определения и ответы'), ('4', 'Последовательность')], max_length=150),
        ),
    ]