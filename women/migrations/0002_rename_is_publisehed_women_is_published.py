# Generated by Django 4.0.5 on 2022-06-22 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='women',
            old_name='is_publisehed',
            new_name='is_published',
        ),
    ]