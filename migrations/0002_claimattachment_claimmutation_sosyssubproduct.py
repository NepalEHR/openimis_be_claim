# Generated by Django 2.1.14 on 2021-05-09 16:47

import core.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_mutationlog_client_mutation_details'),
        ('claim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimAttachment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('validity_from', core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now)),
                ('validity_to', core.fields.DateTimeField(blank=True, db_column='ValidityTo', null=True)),
                ('legacy_id', models.UUIDField(blank=True, db_column='LegacyID', null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('date', core.fields.DateField(blank=True, null=True)),
                ('filename', models.TextField(blank=True, null=True)),
                ('mime', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('document', models.TextField(blank=True, null=True)),
                ('claim', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='attachments', to='claim.Claim')),
            ],
            options={
                'db_table': 'claim_ClaimAttachment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClaimMutation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('claim', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mutations', to='claim.Claim')),
                ('mutation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='claims', to='core.MutationLog')),
            ],
            options={
                'db_table': 'claim_ClaimMutation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SosysSubProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sch_name', models.CharField(db_column='sch_name', max_length=100)),
                ('sch_name_eng', models.CharField(db_column='sch_name_eng', max_length=100)),
                ('status', models.BooleanField(blank=True, db_column='status', null=True)),
                ('product_id', models.IntegerField(db_column='product_id')),
                ('sosys_type', models.CharField(db_column='type', max_length=1)),
            ],
            options={
                'db_table': 'sosys_subproduct',
            },
        ),
    ]
