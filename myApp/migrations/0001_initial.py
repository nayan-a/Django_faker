# Generated by Django 4.0.1 on 2024-06-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
