# Generated by Django 3.0.1 on 2019-12-19 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vc', '0007_auto_20191219_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit_table',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
