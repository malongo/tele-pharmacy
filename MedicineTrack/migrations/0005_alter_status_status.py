# Generated by Django 4.0.4 on 2022-09-10 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicineTrack', '0004_ordermedicine_created_at_ordermedicine_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
