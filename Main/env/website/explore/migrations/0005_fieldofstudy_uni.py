# Generated by Django 3.1 on 2023-12-07 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0004_auto_20231207_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldofstudy',
            name='uni',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fields_of_study', to='explore.university'),
            preserve_default=False,
        ),
    ]
