# Generated by Django 3.2 on 2021-07-05 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0012_transaction_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holding',
            name='stock_symbol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.tsxstock'),
        ),
    ]