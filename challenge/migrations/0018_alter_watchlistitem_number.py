# Generated by Django 3.2 on 2021-07-12 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0017_auto_20210712_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlistitem',
            name='number',
            field=models.IntegerField(),
        ),
    ]
