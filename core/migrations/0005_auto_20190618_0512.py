# Generated by Django 2.2.2 on 2019-06-18 05:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190618_0423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_stats',
            name='book',
        ),
        migrations.RemoveField(
            model_name='book_stats',
            name='words',
        ),
        migrations.AddField(
            model_name='word',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Book'),
        ),
        migrations.CreateModel(
            name='Book_Raw_Text',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Book')),
            ],
        ),
    ]
