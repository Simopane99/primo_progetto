# Generated by Django 5.1.3 on 2025-02-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corsi_formazione', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corso',
            name='titolo',
            field=models.CharField(max_length=30),
        ),
    ]
