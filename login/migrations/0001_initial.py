# Generated by Django 3.2 on 2021-06-04 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=50)),
                ('Pwd', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=1)),
                ('MartialStatus', models.CharField(max_length=50)),
            ],
        ),
    ]
