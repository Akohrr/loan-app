# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('installments', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('declined', 'Declined')], default='pending', max_length=8)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_author', to='account.Profile')),
                ('guarantor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='loan_guarantor', to='account.Profile')),
            ],
        ),
    ]
