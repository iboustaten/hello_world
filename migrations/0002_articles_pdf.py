# Generated by Django 3.1 on 2020-10-11 15:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='PDF',
            field=models.FileField(default=django.utils.timezone.now, upload_to='pdfs/'),
            preserve_default=False,
        ),
    ]
