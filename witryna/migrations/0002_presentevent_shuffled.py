# Generated by Django 3.1.4 on 2021-01-09 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('witryna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentevent',
            name='shuffled',
            field=models.CharField(default='no', max_length=20),
        ),
    ]