# Generated by Django 3.0.7 on 2021-05-03 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0005_studentresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
    ]
