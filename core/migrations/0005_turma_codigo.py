# Generated by Django 2.1.4 on 2018-12-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_professor_turma'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='codigo',
            field=models.IntegerField(default=1),
        ),
    ]
