# Generated by Django 4.1.7 on 2023-05-15 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_ticket_cust_signature_ticket_tech_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='cust_signature',
            field=models.ImageField(blank=True, null=True, upload_to='signatures/'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='tech_signature',
            field=models.ImageField(blank=True, null=True, upload_to='signatures/'),
        ),
    ]