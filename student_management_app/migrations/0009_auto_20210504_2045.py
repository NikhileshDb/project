# Generated by Django 3.0.7 on 2021-05-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0008_auto_20210504_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='is_featured',
            field=models.TextField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]