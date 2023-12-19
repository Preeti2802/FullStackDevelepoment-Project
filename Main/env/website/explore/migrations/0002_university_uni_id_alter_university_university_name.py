# Generated by Django 5.0 on 2023-12-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='uni_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='university',
            name='university_name',
            field=models.CharField(max_length=255),
        ),
    ]