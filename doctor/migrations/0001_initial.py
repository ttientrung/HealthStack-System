# Generated by Django 4.0.6 on 2022-08-09 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_Information',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('degree', models.TextField(blank=True, null=True)),
                ('department', models.CharField(blank=True, choices=[('Cardiologists', 'Cardiologists'), ('Neurologists', 'Neurologists'), ('Pediatricians', 'Pediatricians'), ('Physiatrists', 'Physiatrists'), ('Dermatologists', 'Dermatologists')], max_length=200, null=True)),
                ('featured_image', models.ImageField(blank=True, default='doctors/user-default.png', null=True, upload_to='doctors/')),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('visiting_hour', models.TextField(blank=True, null=True)),
                ('consultation_fee', models.IntegerField(blank=True, null=True)),
                ('report_fee', models.IntegerField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('hospital_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital_information')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]