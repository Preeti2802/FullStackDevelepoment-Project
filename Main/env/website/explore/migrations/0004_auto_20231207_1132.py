# Generated by Django 3.1 on 2023-12-07 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0003_remove_programs_loc'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldofstudy',
            name='fos_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fieldofstudy',
            name='fos_name',
            field=models.CharField(max_length=255),
        ),
    ]