

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
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('photo', models.ImageField(null=True, upload_to='pics/', verbose_name='Medicine photo')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('status', models.BooleanField(default=True)),
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
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('city', models.CharField(choices=[('DOM', 'DODOMA'), ('DSM', 'DAR-ES-SALAAM'), ('ARS', 'ARUSHA'), ('MBY', 'MBEYA'), ('KLM', 'KILIMANJARO'), ('BKB', 'BUKOBA'), ('IRI', 'IRINGA'), ('NJO', 'NJOMBE')], max_length=3)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=30)),
                ('order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MedicineTrack.order')),
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
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=100)),
                ('Status', models.BooleanField(default=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicineTrack.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('medicine_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MedicineTrack.medicine')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicineTrack.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='retail_id',
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
