# Generated by Django 3.2.8 on 2022-04-07 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_delete_courseold'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'ordering': ['start'], 'verbose_name': 'palestra', 'verbose_name_plural': 'palestras'},
        ),
    ]
