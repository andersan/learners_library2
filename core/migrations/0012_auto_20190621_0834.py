# Generated by Django 2.2.2 on 2019-06-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190621_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_readability',
            name='smog_index',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
