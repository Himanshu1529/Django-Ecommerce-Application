# Generated by Django 4.2.7 on 2024-01-30 14:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_remove_orderitems_status_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tracking_id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=20, unique=True),
        ),
    ]
