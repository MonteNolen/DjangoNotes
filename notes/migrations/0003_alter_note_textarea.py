# Generated by Django 4.0.2 on 2022-02-10 19:30

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_note_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='textarea',
            field=tinymce.models.HTMLField(max_length=1000, verbose_name='Поле для отчета'),
        ),
    ]
