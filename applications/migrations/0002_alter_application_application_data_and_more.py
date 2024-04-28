# Generated by Django 4.2.4 on 2024-04-28 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_data',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='application',
            name='deposit',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='application',
            name='private',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]