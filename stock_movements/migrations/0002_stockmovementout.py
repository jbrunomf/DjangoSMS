# Generated by Django 5.1.5 on 2025-02-02 04:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('stock_movements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockMovementOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_movements_out', to='products.product')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
