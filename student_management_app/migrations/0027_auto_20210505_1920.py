# Generated by Django 3.0.7 on 2021-05-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0026_auto_20210505_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Publish', 'Publish')], default='Draft', max_length=10),
        ),
    ]
