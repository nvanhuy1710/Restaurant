# Generated by Django 5.0.4 on 2024-05-14 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField()),
                ('image', models.ImageField(upload_to='assets/images/')),
            ],
        ),
    ]
