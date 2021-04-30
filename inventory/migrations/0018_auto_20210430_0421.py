# Generated by Django 3.1.7 on 2021-04-30 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_auto_20210429_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='acquisition_date',
            field=models.DateField(blank=True, null=True, verbose_name='Acquisition date'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='purchase_date',
            field=models.DateField(blank=True, null=True, verbose_name='Purchase date'),
        ),
    ]
