# Generated by Django 2.0.4 on 2018-04-26 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lagscrumy', '0003_auto_20180426_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumygoals',
            name='goalstatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lagscrumy.GoalStatus'),
        ),
    ]
