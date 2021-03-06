# Generated by Django 2.2.2 on 2019-06-18 04:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190618_0415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=31)),
                ('count', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='book_stats',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Book'),
        ),
        migrations.AddField(
            model_name='book_stats',
            name='words',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Word'),
        ),
    ]
