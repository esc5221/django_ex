# Generated by Django 4.0.6 on 2022-08-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0002_userseminar'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='nullable_capacity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
