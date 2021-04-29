# Generated by Django 3.1.3 on 2021-04-22 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='adress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='zipcode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
