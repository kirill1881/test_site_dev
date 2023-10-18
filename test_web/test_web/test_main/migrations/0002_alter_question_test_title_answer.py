# Generated by Django 4.2.6 on 2023-10-18 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='test_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_main.test'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_answer', models.CharField(max_length=150)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_main.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_main.user')),
            ],
        ),
    ]