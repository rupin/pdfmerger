# Generated by Django 2.1.3 on 2019-06-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfmerge', '0007_auto_20190618_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='field_description',
            field=models.CharField(default='', max_length=200),
        ),
    ]