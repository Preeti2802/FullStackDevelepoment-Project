# Generated by Django 3.1 on 2023-12-13 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0008_fieldofstudy_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldofstudy',
            name='cat',
        ),
        migrations.AddField(
            model_name='fieldofstudy',
            name='cat',
            field=models.ManyToManyField(related_name='fields_of_study', to='explore.Category'),
        ),
        migrations.RemoveField(
            model_name='university',
            name='cat',
        ),
        migrations.AddField(
            model_name='university',
            name='cat',
            field=models.ManyToManyField(related_name='universities', to='explore.Category'),
        ),
    ]
