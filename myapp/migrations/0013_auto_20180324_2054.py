# Generated by Django 2.0.3 on 2018-03-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20180324_2040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={},
        ),
        migrations.AlterField(
            model_name='page',
            name='position',
            field=models.IntegerField(),
        ),
    ]
