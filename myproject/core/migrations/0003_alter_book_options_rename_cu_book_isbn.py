# Generated by Django 4.2 on 2024-05-26 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='cu',
            new_name='isbn',
        ),
    ]
