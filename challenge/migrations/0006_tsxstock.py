# Generated by Django 3.2 on 2021-05-27 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0005_watchlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='TSXStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
