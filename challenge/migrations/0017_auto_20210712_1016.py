# Generated by Django 3.2 on 2021-07-12 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0016_auto_20210709_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='txn_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='watchlistitem',
            name='date_added',
            field=models.DateField(),
        ),
    ]