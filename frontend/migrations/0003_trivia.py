# Generated by Django 4.2.13 on 2024-05-24 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_character'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trivia', to='frontend.planet')),
            ],
        ),
    ]
