# Generated by Django 3.2.23 on 2023-12-08 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0005_debitnotetransactionhistory_purchasedebit_purchasedebit1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sub_total', models.FloatField(default='')),
                ('cgst', models.FloatField(default='')),
                ('sgst', models.FloatField(default='')),
                ('tax_amount', models.FloatField(default='')),
                ('adjustment', models.FloatField(default='')),
                ('total', models.FloatField(default='')),
                ('paid', models.FloatField(default='')),
                ('balance', models.FloatField(default='')),
                ('payment_type', models.CharField(default='', max_length=200)),
                ('expense_date', models.DateField(auto_now_add=True, null=True)),
                ('EXP_NO', models.IntegerField(default=0)),
                ('action', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Expense_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.CharField(max_length=255)),
                ('tax', models.FloatField(default='')),
                ('amount', models.FloatField(default='')),
                ('expense_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.expense')),
            ],
        ),
        migrations.CreateModel(
            name='Expense_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_category', models.CharField(max_length=200)),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.staff_details')),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.expense_category'),
        ),
        migrations.AddField(
            model_name='expense',
            name='party_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.party'),
        ),
        migrations.AddField(
            model_name='expense',
            name='staff_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.staff_details'),
        ),
    ]
