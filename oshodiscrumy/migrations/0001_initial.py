# Generated by Django 2.0.4 on 2018-05-21 22:57

from django.db import migrations, models
import django.db.models.deletion
import oshodiscrumy.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Goal Status',
            },
        ),
        migrations.CreateModel(
            name='ScrumyGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.TextField()),
                ('goal_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oshodiscrumy.GoalStatus')),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, validators=[oshodiscrumy.validators.validate_username_length, oshodiscrumy.validators.validate_username_alphadigits], verbose_name='Username')),
                ('password1', models.CharField(max_length=30, validators=[oshodiscrumy.validators.validate_password_length])),
                ('password2', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Developer'), (2, 'Admin'), (3, 'QA - Quality Analyst'), (4, 'Owner')])),
            ],
            options={
                'verbose_name_plural': 'Scrumy User',
                'permissions': (('can_move_anywhere', 'Can move from anywhere to anywhere'), ('move_from_DT_to_verify', 'Can move from dailytask to Verify'), ('move_from_verify_to_done', 'Can move from verify to Done'), ('move_from_WG_to_DT', 'Can move from weeklygoal to dailytask')),
            },
        ),
        migrations.AddField(
            model_name='scrumygoals',
            name='scrumy_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oshodiscrumy.ScrumyUser'),
        ),
    ]
