# Generated by Django 2.2.24 on 2021-12-26 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0004_remove_neighbourhood_admin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NeighbourHood',
            new_name='Hood',
        ),
    ]
