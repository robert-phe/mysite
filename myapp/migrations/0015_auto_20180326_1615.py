# Generated by Django 2.0.3 on 2018-03-26 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20180324_2153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['position']},
        ),
    ]