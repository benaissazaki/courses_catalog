# Generated by Django 4.1.2 on 2022-10-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_exam_created_at'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='exam',
            name='course_or_category',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='category',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='related_course',
        ),
        migrations.AddField(
            model_name='exam',
            name='categories',
            field=models.ManyToManyField(to='courses.category'),
        ),
        migrations.AddField(
            model_name='exam',
            name='related_courses',
            field=models.ManyToManyField(to='courses.course'),
        ),
    ]
