# Generated by Django 4.1.2 on 2022-10-10 15:09

import courses.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='courses', validators=[courses.validators.PDFFileValidator(max_size=52428800)]),
        ),
    ]