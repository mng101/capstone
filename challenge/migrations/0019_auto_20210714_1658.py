# Generated by Django 3.2 on 2021-07-14 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0018_alter_watchlistitem_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-txn_date', 'symbol']},
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='stock_symbol',
            new_name='symbol',
        ),
    ]
