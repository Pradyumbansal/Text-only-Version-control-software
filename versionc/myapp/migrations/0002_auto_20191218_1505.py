# Generated by Django 3.0 on 2019-12-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sha_table',
            name='sha',
            field=models.CharField(max_length=50),
        ),
    ]
