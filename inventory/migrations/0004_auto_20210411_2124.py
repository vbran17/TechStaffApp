# Generated by Django 3.1.7 on 2021-04-11 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210410_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='acquistion_date',
            new_name='acquisition_date',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='pdate',
            field=models.DateField(blank=True),
        ),
    ]
