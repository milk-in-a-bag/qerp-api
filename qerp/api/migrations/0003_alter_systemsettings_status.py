# Generated by Django 5.0 on 2024-02-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_systemsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemsettings',
            name='status',
            field=models.CharField(choices=[('In stock', 'In stock'), ('On backorder', 'On backorder'), ('In transit', 'In transit'), ('Allocated', 'Allocated'), ('Shipped', 'Shipped')]),
        ),
    ]
