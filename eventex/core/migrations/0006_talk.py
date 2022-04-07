# Generated by Django 3.2.8 on 2022-04-06 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220406_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start', models.TimeField()),
                ('description', models.TextField()),
                ('speakers', models.ManyToManyField(to='core.Speaker')),
            ],
        ),
    ]