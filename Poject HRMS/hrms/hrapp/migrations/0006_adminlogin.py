# Generated by Django 4.0 on 2022-01-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0005_remove_registration_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
