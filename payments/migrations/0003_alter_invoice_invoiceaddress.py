# Generated by Django 3.2.2 on 2021-05-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_invoice_invoiceaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoiceAddress',
            field=models.CharField(max_length=250),
        ),
    ]
