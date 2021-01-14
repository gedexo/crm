# Generated by Django 3.1.4 on 2021-01-14 04:43

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('auto_id', models.PositiveIntegerField(db_index=True, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_sale_objects', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(limit_choices_to={'is_deleted': False}, on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('updater', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='updator_sale_objects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'sale',
                'verbose_name_plural': 'sales',
                'db_table': 'sales_sale',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('product', models.ForeignKey(limit_choices_to={'is_deleted': False}, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.sale')),
            ],
            options={
                'verbose_name': 'sale item',
                'verbose_name_plural': 'sale items',
                'db_table': 'sales_sale item',
                'ordering': ('sale',),
            },
        ),
    ]
