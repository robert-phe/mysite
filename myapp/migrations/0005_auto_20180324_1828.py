# Generated by Django 2.0.3 on 2018-03-24 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_question_test_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='test_name',
            new_name='page',
        ),
    ]
