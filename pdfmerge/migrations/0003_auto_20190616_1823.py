# Generated by Django 2.1.3 on 2019-06-16 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfmerge', '0002_auto_20190616_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='field_type',
        ),
        migrations.AddField(
            model_name='userdata',
            name='field_type',
            field=models.ManyToManyField(default=0, to='pdfmerge.FormField'),
        ),
    ]