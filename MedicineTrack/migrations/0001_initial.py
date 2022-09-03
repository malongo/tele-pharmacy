# Generated by Django 4.0.4 on 2022-09-03 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=400)),
                ('photo', models.ImageField(null=True, upload_to='pics/', verbose_name='Medicine photo')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Retail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneNumber_1', models.CharField(max_length=15)),
                ('PhoneNumber_2', models.CharField(max_length=15, null=True)),
                ('Country', django_countries.fields.CountryField(max_length=2)),
                ('City', models.CharField(choices=[('Ars', 'Arusha'), ('Bkb', 'Bukoba'), ('Dsm', 'Dar es salaam'), ('Mwz', 'Mwanza'), ('Dom', 'Dodoma'), ('klm', 'Kilimanjaro'), ('Irg', 'Iringa'), ('Njo', 'Njombe'), ('Tng', 'Tanga'), ('Mby', 'Mbeya'), ('Mor', 'Morogoro'), ('Sng', 'Singida')], max_length=3)),
                ('Address', models.CharField(max_length=254)),
                ('RetailEmail', models.EmailField(max_length=254)),
                ('OrganizationName', models.CharField(max_length=254)),
                ('Status', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(default=True, max_length=100, unique=True)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('city', models.CharField(choices=[('DOM', 'DODOMA'), ('DSM', 'DAR-ES-SALAAM'), ('ARS', 'ARUSHA'), ('MBY', 'MBEYA'), ('KLM', 'KILIMANJARO'), ('BKB', 'BUKOBA'), ('IRI', 'IRINGA'), ('NJO', 'NJOMBE')], max_length=3)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=30)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicineTrack.order')),
                ('retail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MedicineTrack.retail')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicineTrack.order')),
                ('status_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='MedicineTrack.status')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('total_price', models.FloatField(null=True)),
                ('medicine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MedicineTrack.medicine')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicineTrack.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='retail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicineTrack.retail'),
        ),
        migrations.CreateModel(
            name='MedicinePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('status', models.BooleanField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicineTrack.medicine')),
            ],
        ),
    ]
