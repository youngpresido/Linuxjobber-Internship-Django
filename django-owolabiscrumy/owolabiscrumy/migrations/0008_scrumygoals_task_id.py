# Generated by Django 2.0.4 on 2018-04-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owolabiscrumy', '0007_auto_20180423_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrumygoals',
            name='task_id',
            field=models.IntegerField(default=700),
        ),
    ]
