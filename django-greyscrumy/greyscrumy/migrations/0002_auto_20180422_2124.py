# Generated by Django 2.0.4 on 2018-04-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greyscrumy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumygoals',
            name='date_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
