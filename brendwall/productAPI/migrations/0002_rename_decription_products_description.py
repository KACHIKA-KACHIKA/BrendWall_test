# Generated by Django 5.1.1 on 2024-09-10 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='decription',
            new_name='description',
        ),
    ]
