# Generated by Django 3.2.3 on 2021-05-31 18:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0002_auto_20210531_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]