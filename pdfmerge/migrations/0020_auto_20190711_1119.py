# Generated by Django 2.1.3 on 2019-07-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfmerge', '0019_field_field_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdfformfield',
            name='field_choice',
        ),
        migrations.AddField(
            model_name='field',
            name='field_choice',
            field=models.CharField(choices=[('NONE', 'NONE'), ('FULLDATE', 'FULLDATE'), ('DATE', 'DATE'), ('MONTH', 'MONTH'), ('YEAR', 'YEAR'), ('FULLDATE_TEXT_MONTH', 'FULLDATE_TEXT_MONTH'), ('CHECK_BOX', 'CHECK_BOX')], default='NONE', max_length=20),
        ),
    ]
