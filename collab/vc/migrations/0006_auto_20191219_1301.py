# Generated by Django 3.0.1 on 2019-12-19 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vc', '0005_auto_20191219_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit_table',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commit_table',
            name='code',
            field=models.CharField(max_length=50),
        ),
    ]