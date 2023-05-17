# Generated by Django 4.1.7 on 2023-05-13 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.DateField(blank=True, null=True)),
                ('jobno', models.CharField(blank=True, max_length=30, null=True)),
                ('jobname', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=60, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zip', models.IntegerField(blank=True, null=True)),
                ('auth_by', models.CharField(blank=True, max_length=30, null=True)),
                ('report_to', models.CharField(blank=True, max_length=30, null=True)),
                ('man1', models.CharField(blank=True, max_length=70, null=True)),
                ('man2', models.CharField(blank=True, max_length=70, null=True)),
                ('man3', models.CharField(blank=True, max_length=70, null=True)),
                ('model1', models.CharField(blank=True, max_length=70, null=True)),
                ('model2', models.CharField(blank=True, max_length=70, null=True)),
                ('model3', models.CharField(blank=True, max_length=70, null=True)),
                ('serial1', models.CharField(blank=True, max_length=70, null=True)),
                ('serial2', models.CharField(blank=True, max_length=70, null=True)),
                ('serial3', models.CharField(blank=True, max_length=70, null=True)),
                ('unit1', models.IntegerField(blank=True, null=True)),
                ('unit2', models.IntegerField(blank=True, null=True)),
                ('unit3', models.IntegerField(blank=True, null=True)),
                ('loc1', models.CharField(blank=True, max_length=70, null=True)),
                ('loc2', models.CharField(blank=True, max_length=70, null=True)),
                ('loc3', models.CharField(blank=True, max_length=70, null=True)),
                ('desc', models.TextField(blank=True, max_length=700, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('day', models.CharField(blank=True, choices=[('M', 'MONDAY'), ('TU', 'TUESDAY'), ('W', 'WEDNESDAY'), ('TH', 'THURSDAY'), ('F', 'FRIDAY'), ('SA', 'SATURDAY'), ('SU', 'SUNDAY')], max_length=2, null=True)),
                ('hours', models.IntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, max_length=200, null=True)),
                ('complete', models.BooleanField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Refrigerant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(blank=True, max_length=20, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('tracking', models.CharField(blank=True, max_length=30, null=True)),
                ('new', models.BooleanField(blank=True, null=True)),
                ('recover', models.BooleanField(blank=True, null=True)),
                ('recycle', models.BooleanField(blank=True, null=True)),
                ('reclaim', models.BooleanField(blank=True, null=True)),
                ('rc_ctr', models.CharField(blank=True, max_length=70, null=True)),
                ('po', models.CharField(blank=True, max_length=30, null=True)),
                ('ticket', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='refrigerant', to='tickets.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='Reasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pm', models.BooleanField(blank=True, default=False, null=True, verbose_name='Preventative Maintenance')),
                ('emer', models.BooleanField(blank=True, default=False, null=True, verbose_name='Emergency')),
                ('warr', models.BooleanField(blank=True, default=False, null=True, verbose_name='Warranty')),
                ('start', models.BooleanField(blank=True, default=False, null=True, verbose_name='Startup')),
                ('narep', models.BooleanField(blank=True, default=False, null=True, verbose_name='Non-Agreement Repair')),
                ('inst', models.BooleanField(blank=True, default=False, null=True, verbose_name='Installation')),
                ('other', models.BooleanField(blank=True, default=False, null=True, verbose_name='Other')),
                ('ticket', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reasons', to='tickets.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('desc', models.CharField(blank=True, max_length=70, null=True)),
                ('po', models.CharField(blank=True, max_length=40, null=True)),
                ('stock', models.CharField(blank=True, max_length=70, null=True)),
                ('ticket', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='material', to='tickets.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recovery', models.BooleanField(blank=True, null=True)),
                ('torch', models.BooleanField(blank=True, null=True)),
                ('vacuum', models.BooleanField(blank=True, null=True)),
                ('power', models.BooleanField(blank=True, null=True)),
                ('tube', models.BooleanField(blank=True, null=True)),
                ('rig', models.BooleanField(blank=True, null=True)),
                ('special', models.BooleanField(blank=True, null=True)),
                ('other', models.BooleanField(blank=True, null=True)),
                ('ticket', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='equipment', to='tickets.ticket')),
            ],
        ),
    ]