# Generated by Django 4.0.6 on 2022-09-04 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0016_doctor_information_service_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor_information',
            old_name='service_name',
            new_name='service',
        ),
        migrations.RenameField(
            model_name='doctor_information',
            old_name='specialization_name',
            new_name='specialization',
        ),
    ]