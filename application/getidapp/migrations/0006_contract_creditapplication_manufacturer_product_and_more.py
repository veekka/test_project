# Generated by Django 4.0 on 2021-12-20 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('getidapp', '0005_contracts_creditapplications_manufacturers_products_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Date_create_contract')),
                ('id_contract', models.CharField(max_length=20, unique=True, verbose_name='id_contract')),
            ],
        ),
        migrations.CreateModel(
            name='CreditApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Date_create_application')),
                ('id_application', models.CharField(max_length=20, unique=True, verbose_name='id_application')),
                ('id_contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_id', to='getidapp.contract')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Date_create_manufacturer')),
                ('id_manufacturer', models.CharField(max_length=20, verbose_name='Id_manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Date_create_product')),
                ('name_product', models.CharField(max_length=50, unique=True, verbose_name='Name_product')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='getidapp.creditapplication')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='getidapp.manufacturer')),
            ],
        ),
        migrations.RemoveField(
            model_name='creditapplications',
            name='id_contract',
        ),
        migrations.RemoveField(
            model_name='products',
            name='application',
        ),
        migrations.RemoveField(
            model_name='products',
            name='manufacturer',
        ),
        migrations.DeleteModel(
            name='Contracts',
        ),
        migrations.DeleteModel(
            name='CreditApplications',
        ),
        migrations.DeleteModel(
            name='Manufacturers',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]