# Generated by Django 3.1.3 on 2021-04-22 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210422_0718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='has_history',
        ),
    ]