# Generated by Django 4.0.6 on 2022-08-10 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_alter_patient_address_alter_patient_nid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='history',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
