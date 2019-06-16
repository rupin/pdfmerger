# Generated by Django 2.1.3 on 2019-06-16 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pdfmerge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='field_page_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='formfield',
            name='field_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='formfield',
            name='field_x',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='formfield',
            name='field_x_increment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='formfield',
            name='field_y',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='formfield',
            name='fk_pdf_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pdfmerge.PDFForm'),
        ),
        migrations.AddField(
            model_name='pdfform',
            name='file_path',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='pdfform',
            name='pdf_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='pdfform',
            name='pdf_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdata',
            name='field_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='userdata',
            name='field_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdata',
            name='fk_user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
