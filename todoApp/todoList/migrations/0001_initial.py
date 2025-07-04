# Generated by Django 3.2.25 on 2025-06-23 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('title', models.CharField(
                    'Título',
                    max_length=200
                )),
                ('description', models.TextField(
                    'Descrição',
                    blank=True,
                    null=True
                )),
                ('complete', models.BooleanField(
                    'Concluída',
                    default=False
                )),
                ('created', models.DateTimeField(
                    'Criado em',
                    auto_now_add=True
                )),
            ],
            options={
                'ordering': ['complete', '-created'],
            },
        ),
    ]