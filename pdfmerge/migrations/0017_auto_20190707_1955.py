# Generated by Django 2.1.3 on 2019-07-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfmerge', '0016_pdfform_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfform',
            name='file_path',
            field=models.FileField(default='', upload_to='pdfs'),
        ),
        migrations.AlterField(
            model_name='pdfform',
            name='image',
            field=models.FileField(default='', upload_to='photos'),
        ),
    ]
