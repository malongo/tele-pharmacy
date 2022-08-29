# Generated by Django 4.0.4 on 2022-08-29 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MedicineTrack', '0002_remove_order_order_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('city', models.CharField(choices=[('DOM', 'DODOMA'), ('DSM', 'DAR-ES-SALAAM'), ('ARS', 'ARUSHA'), ('MBY', 'MBEYA'), ('KLM', 'KILIMANJARO'), ('BKB', 'BUKOBA'), ('IRI', 'IRINGA'), ('NJO', 'NJOMBE')], max_length=3)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='status',
            new_name='complete',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='retail_id',
            new_name='retail',
        ),
        migrations.RenameField(
            model_name='ordermedicine',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderstatus',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RemoveField(
            model_name='ordermedicine',
            name='medicine_id',
        ),
        migrations.RemoveField(
            model_name='retail',
            name='user_id',
        ),
        migrations.AddField(
            model_name='ordermedicine',
            name='medicine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MedicineTrack.medicine'),
        ),
        migrations.AddField(
            model_name='retail',
            name='retail',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Shipping',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicineTrack.order'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='retail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MedicineTrack.retail'),
        ),
    ]