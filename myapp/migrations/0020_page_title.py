# Generated by Django 2.0.3 on 2018-03-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_remove_page_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
