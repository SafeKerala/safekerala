# Generated by Django 4.2.17 on 2025-01-18 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewfeedback',
            name='date',
            field=models.DateField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='viewfeedback',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
