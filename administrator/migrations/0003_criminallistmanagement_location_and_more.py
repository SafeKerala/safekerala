# Generated by Django 4.2.17 on 2025-01-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_viewfeedback_date_viewfeedback_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminallistmanagement',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='criminallistmanagement',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
