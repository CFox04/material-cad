# Generated by Django 3.1.7 on 2021-04-05 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('civilian', '0001_initial'),
        ('police', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registry', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CitationReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FlagType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civilian.character')),
                ('officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='police.officer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleCitationReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WarrantType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Arrest',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ncic.record')),
                ('location', models.CharField(max_length=100)),
                ('witness_names', models.CharField(max_length=255)),
                ('incident_summary', models.TextField()),
                ('evidence_found', models.TextField()),
                ('is_felony', models.BooleanField()),
                ('is_gang_related', models.BooleanField()),
                ('weapon_used', models.BooleanField()),
                ('officer_used_force', models.BooleanField()),
            ],
            bases=('ncic.record',),
        ),
        migrations.CreateModel(
            name='Bolo',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ncic.record')),
                ('description', models.CharField(max_length=25)),
            ],
            bases=('ncic.record',),
        ),
        migrations.CreateModel(
            name='Warrant',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ncic.record')),
                ('warrant_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ncic.warranttype')),
            ],
            bases=('ncic.record',),
        ),
        migrations.CreateModel(
            name='VehicleCitation',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ncic.record')),
                ('license_plate', models.CharField(max_length=25)),
                ('vehicle_speed', models.IntegerField(default=0)),
                ('speed_limit', models.IntegerField(default=0)),
                ('details', models.TextField()),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ncic.vehiclecitationreason')),
                ('vehicle_color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registry.vehiclecolor')),
                ('vehicle_make', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registry.vehiclemake')),
                ('vehicle_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registry.vehicletype')),
            ],
            bases=('ncic.record',),
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ncic.record')),
                ('flag_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ncic.flagtype')),
            ],
            bases=('ncic.record',),
        ),
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ncic.record')),
                ('location', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ncic.citationreason')),
            ],
            bases=('ncic.record',),
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ncic.record')),
                ('charge_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ncic.chargetype')),
                ('related_arrest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ncic.arrest')),
            ],
            bases=('ncic.record',),
        ),
    ]
