# Generated by Django 5.0 on 2023-12-05 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0002_university_uni_id_alter_university_university_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programs',
            name='loc',
        ),
    ]