# Generated by Django 4.2.17 on 2025-01-19 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0005_viewworkrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='date',
            field=models.DateField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
