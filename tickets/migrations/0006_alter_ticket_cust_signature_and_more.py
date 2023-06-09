# Generated by Django 4.1.7 on 2023-05-15 23:40

from django.db import migrations
import jsignature.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_alter_ticket_cust_signature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='cust_signature',
            field=jsignature.fields.JSignatureField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='tech_signature',
            field=jsignature.fields.JSignatureField(blank=True, null=True),
        ),
    ]
