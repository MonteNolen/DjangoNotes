# Generated by Django 4.0.2 on 2022-02-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Закрыто?'),
        ),
    ]
