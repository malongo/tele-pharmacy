# Generated by Django 4.0.4 on 2022-08-29 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MedicineTrack', '0003_shippingaddress_rename_status_order_complete_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retail',
            name='retail',
        ),
        migrations.AddField(
            model_name='retail',
            name='user',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
