# Generated by Django 4.0.6 on 2022-08-02 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0001_squashed_0005_seminar_blankable_desc'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='seminars',
            field=models.ManyToManyField(through='seminar.UserSeminar', to='seminar.seminar'),
        ),
    ]
