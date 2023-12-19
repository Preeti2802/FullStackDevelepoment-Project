# Generated by Django 4.2.8 on 2023-12-14 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0013_programs_university_programs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldofstudy',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='university',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='university',
            name='locations',
        ),
        migrations.RemoveField(
            model_name='university',
            name='programs',
        ),
        migrations.AddField(
            model_name='fieldofstudy',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fields_of_study', to='explore.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='universities', to='explore.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='loc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='universities', to='explore.location'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Programs',
        ),
    ]