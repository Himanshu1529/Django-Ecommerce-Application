# Generated by Django 4.2.7 on 2024-01-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_remove_order_status_remove_order_track_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='status',
            field=models.CharField(choices=[('Ordered', 'Ordered'), ('Shipping', 'Order Shipping'), ('Way', 'On the Way'), ('Completed', 'Order Completed')], default='Ordered', max_length=20, null=True),
        ),
    ]
