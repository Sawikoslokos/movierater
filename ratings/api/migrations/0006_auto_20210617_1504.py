# Generated by Django 3.2.4 on 2021-06-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210617_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktor',
            name='filmy',
            field=models.ManyToManyField(related_name='aktorzy', to='api.Film'),
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzajFilmu',
            field=models.IntegerField(choices=[(3, 'Komedia'), (1, 'Dramat'), (0, 'Nieznany'), (2, 'Sci-Fi')]),
        ),
        migrations.AlterField(
            model_name='film',
            name='opis',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
    ]
