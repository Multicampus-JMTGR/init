# Generated by Django 3.1.2 on 2020-11-06 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201105_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyplan',
            name='email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
