# Generated by Django 2.1.3 on 2019-07-10 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfmerge', '0018_field_field_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='field_state',
            field=models.CharField(choices=[('DYNAMIC', 'DYNAMIC'), ('STATIC', 'STATIC')], default='STATIC', max_length=20),
        ),
    ]
