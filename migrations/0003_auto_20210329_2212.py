# Generated by Django 2.1.14 on 2021-03-29 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claim', '0002_claimattachment_claimmutation_sosyssubproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sosyssubproduct',
            name='product_id',
            field=models.IntegerField(db_column='product_id'),
        ),
    ]
