# Generated by Django 2.1.3 on 2019-07-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfmerge', '0021_auto_20190711_1119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pdfform',
            options={'ordering': ('pdf_name',)},
        ),
        migrations.AddField(
            model_name='field',
            name='field_category',
            field=models.CharField(choices=[('PERSONAL', 'Personal')], default='PERSONAL', max_length=20),
        ),
    ]
