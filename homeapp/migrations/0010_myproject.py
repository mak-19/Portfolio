# Generated by Django 3.0.4 on 2020-10-11 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0009_auto_20201011_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.TextField()),
                ('p2', models.TextField()),
                ('p3', models.TextField()),
                ('p4', models.TextField()),
            ],
        ),
    ]
