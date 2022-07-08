# Generated by Django 4.0 on 2022-07-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Interview_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]