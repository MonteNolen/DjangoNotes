# Generated by Django 4.0.2 on 2022-02-13 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_alter_note_textarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.noteauthor', verbose_name='Пользователь'),
        ),
    ]