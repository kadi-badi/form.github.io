# Generated by Django 3.1.5 on 2021-02-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(default='', max_length=50)),
                ('question2', models.CharField(default='', max_length=50)),
                ('question3', models.CharField(default='', max_length=50)),
                ('question4', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
