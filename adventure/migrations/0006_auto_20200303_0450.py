# Generated by Django 3.0.3 on 2020-03-03 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0005_auto_20200302_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monster',
            old_name='honeyGained',
            new_name='xeritesGained',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='honeyLost',
            new_name='xeritesLost',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='honey',
            new_name='xerites',
        ),
    ]