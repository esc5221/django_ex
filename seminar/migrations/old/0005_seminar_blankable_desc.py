# Generated by Django 4.0.6 on 2022-08-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0004_seminar_blankable_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='blankable_desc',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]