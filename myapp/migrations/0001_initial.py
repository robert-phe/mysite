# Generated by Django 2.0.3 on 2018-03-24 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='test_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Test', to_field='test_name'),
        ),
    ]