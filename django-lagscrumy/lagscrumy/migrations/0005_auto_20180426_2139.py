# Generated by Django 2.0.4 on 2018-04-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lagscrumy', '0004_auto_20180426_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumygoals',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
