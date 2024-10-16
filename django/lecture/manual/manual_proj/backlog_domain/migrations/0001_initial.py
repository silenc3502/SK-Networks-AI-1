# Generated by Django 5.0.6 on 2024-10-07 00:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BacklogDomain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('domain', models.CharField(blank=True, max_length=255, null=True)),
                ('backlog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='backlog.backlog')),
            ],
            options={
                'db_table': 'backlog_domain',
            },
        ),
    ]