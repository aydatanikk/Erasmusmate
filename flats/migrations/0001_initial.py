# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 16:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=200)),
                ('place', models.CharField(choices=[('AGH', 'NEAR AGH'), ('KAZIMIERZ', 'IN KAZIMIERZ'), ('OLD TOWN', 'IN STARE MIASTO')], default='', max_length=15)),
                ('adress', models.CharField(blank=True, default='', max_length=50)),
                ('price', models.IntegerField(blank=True, default=0)),
                ('smoker', models.CharField(choices=[("Don't care", "Don't care"), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=10)),
                ('same_nationality_roommates', models.CharField(choices=[("Don't care", "Don't care"), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=10)),
                ('time_of_staying_in_flat', models.CharField(choices=[('1 MONTH', '1 MONTH'), ('2 MONTHS', '2 MONTHS'), ('3 MONTHS', '3 MONTHS'), ('4 MONTHS', '4 MONTHS'), ('5 MONTHS ', '5 MONTHS'), ('6 MONTHS ', '6 MONTHS')], default='', max_length=10)),
                ('num_of_people_total', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], default='', max_length=10)),
                ('num_of_people_available', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], default='', max_length=10)),
                ('men_or_women_on_room', models.CharField(choices=[("Don't care", "Don't care"), ('Men only', 'Men only'), ('Women only', 'Women only')], default='', max_length=10)),
                ('couples_accepted', models.CharField(choices=[("Don't care", "Don't care"), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=10)),
                ('image', models.ImageField(blank=True, default='', upload_to='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
