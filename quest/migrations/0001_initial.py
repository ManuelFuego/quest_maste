# Generated by Django 3.2.4 on 2021-06-24 19:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question', models.CharField(db_index=True, max_length=250)),
                ('question_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('weight', models.FloatField(default=1)),
            ],
            options={
                'verbose_name': 'Тесты',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=250)),
                ('answer_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('is_right', models.BooleanField(default=False)),
                ('question', models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='quest.question')),
            ],
            options={
                'verbose_name': 'Вариант ответа',
                'verbose_name_plural': 'Варианты ответа',
            },
        ),
    ]
