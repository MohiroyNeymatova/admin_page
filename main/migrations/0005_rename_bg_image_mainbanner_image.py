# Generated by Django 4.1.6 on 2023-12-04 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_resources'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainbanner',
            old_name='bg_image',
            new_name='image',
        ),
    ]
