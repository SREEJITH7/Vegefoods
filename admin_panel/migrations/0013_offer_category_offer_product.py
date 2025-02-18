# Generated by Django 5.1.2 on 2024-12-18 08:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0012_remove_catogery_offers_remove_product_offers'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='admin_panel.catogery'),
        ),
        migrations.AddField(
            model_name='offer',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='admin_panel.product'),
        ),
    ]
