# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=256)),
                ('course', models.CharField(help_text=b'Course Name e.g B.TECH/BCA etc.', max_length=100)),
                ('year', models.CharField(help_text=b'year e.g 2011 etc.', max_length=4)),
                ('passout_year', models.CharField(help_text=b'Enter year e.g 2015 etc.', max_length=4)),
                ('aggregate_percentage', models.IntegerField(help_text=b'Enter the Percentage s')),
            ],
            options={
                'ordering': ['-full_name'],
                'verbose_name': 'Student Information',
                'verbose_name_plural': 'Students Information',
            },
        ),
    ]
