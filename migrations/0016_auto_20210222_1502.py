# Generated by Django 2.1.14 on 2021-02-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claim', '0015_auto_20210222_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ssfscheme',
            name='SCH_ID',
        ),
        migrations.AlterField(
            model_name='ssfscheme',
            name='id',
            field=models.AutoField(db_column='SCH_ID', primary_key=True, serialize=False),
        ),
    ]
