# Generated by Django 5.0.6 on 2024-05-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=100)),
                ('answer_text', models.CharField(max_length=100)),
                ('answer_date', models.DateField()),
            ],
        ),
    ]
