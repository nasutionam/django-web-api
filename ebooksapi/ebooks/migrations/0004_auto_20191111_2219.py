# Generated by Django 2.2.7 on 2019-11-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0003_auto_20191111_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
    ]
