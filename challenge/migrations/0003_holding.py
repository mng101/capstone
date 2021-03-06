# Generated by Django 3.2 on 2021-05-10 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0002_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_symbol', models.CharField(max_length=6)),
                ('company_name', models.CharField(max_length=64)),
                ('no_of_shares_owned', models.IntegerField(default=0)),
                ('average_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holdings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
