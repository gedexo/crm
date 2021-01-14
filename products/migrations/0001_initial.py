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
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('auto_id', models.PositiveIntegerField(db_index=True, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('stock', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_product_objects', to=settings.AUTH_USER_MODEL)),
                ('updater', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='updator_product_objects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'products_product',
                'ordering': ('-date_added', 'name'),
            },
        ),
    ]
