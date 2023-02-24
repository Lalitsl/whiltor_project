# Generated by Django 4.1.3 on 2023-01-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=240, unique=True)),
                ('data', models.CharField(max_length=240)),
            ],
        ),
    ]