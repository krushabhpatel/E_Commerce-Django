# Generated by Django 4.2.1 on 2023-05-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=20)),
                ('categoryImage', models.ImageField(upload_to='category')),
            ],
        ),
    ]