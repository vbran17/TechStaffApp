# Generated by Django 3.1.7 on 2021-04-28 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_auto_20210428_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='ipv6_prefix',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='IPv6 prefix'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='checkoutdate',
            field=models.DateField(auto_now_add=True, verbose_name='Checkout date'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='acquisition_date',
            field=models.DateField(blank=True, verbose_name='Acquisition date'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='cs_tag',
            field=models.CharField(blank=True, max_length=255, verbose_name='CS tag'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='mail_exchange',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, related_name='MailExchangeHostname', to='inventory.hostname', verbose_name='Mail exchange'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='purchase_date',
            field=models.DateField(blank=True, verbose_name='Purchase date'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='purchase_order',
            field=models.CharField(blank=True, max_length=255, verbose_name='Purchase order'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='purchase_value',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Purchase value'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='serial_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='Serial number'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='vt_tag',
            field=models.CharField(blank=True, max_length=255, verbose_name='VT tag'),
        ),
        migrations.AlterField(
            model_name='history',
            name='execution_time',
            field=models.TimeField(auto_now_add=True, verbose_name='Execution time'),
        ),
        migrations.AlterField(
            model_name='inventoryuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='ip',
            name='in_use',
            field=models.BooleanField(verbose_name='In use'),
        ),
        migrations.AlterField(
            model_name='ip',
            name='ip_type',
            field=models.CharField(choices=[('I4', 'IPv4'), ('I6', 'IPv6')], default='I4', max_length=2, verbose_name='IP type'),
        ),
    ]
