# Generated by Django 3.2 on 2021-07-09 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0014_alter_transaction_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7),
        ),
    ]
