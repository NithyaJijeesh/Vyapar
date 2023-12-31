# Generated by Django 3.2.23 on 2023-12-13 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vyaparapp', '0012_paymentoutdetails_paymentouthistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_no', models.BigIntegerField(null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('party_name', models.CharField(max_length=150)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_address', models.TextField()),
                ('description', models.TextField()),
                ('payment_type', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('payment_method', models.CharField(max_length=100, null=True)),
                ('payment_acc_number', models.BigIntegerField(null=True)),
                ('payment_cheque_id', models.CharField(max_length=20, null=True)),
                ('payment_upi_id', models.CharField(max_length=20, null=True)),
                ('total_amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('payment_received', models.FloatField(blank=True, default=0.0, null=True)),
                ('balance', models.FloatField(blank=True, default=0.0, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company')),
                ('party', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.party')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.staff_details')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('Created', 'Created'), ('Updated', 'Updated')], max_length=20, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company')),
                ('payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.paymentin')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.staff_details')),
            ],
        ),
        migrations.CreateModel(
            name='DeletedPaymentIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_no', models.BigIntegerField(null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.staff_details')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
