# Generated by Django 2.2.3 on 2019-07-22 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190722_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='word_counter',
            name='book',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='word_counter', to='core.Book'),
            preserve_default=False,
        ),
    ]
