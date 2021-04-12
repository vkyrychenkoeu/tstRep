# Generated by Django 3.1.7 on 2021-04-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('second_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('occupation', models.CharField(default='', max_length=150)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone_number', models.CharField(default='', max_length=12)),
            ],
        ),
    ]