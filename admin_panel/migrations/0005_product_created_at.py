# Generated by Django 5.1.2 on 2024-11-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0004_catogery_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
