# Generated by Django 4.0.6 on 2022-08-08 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almuerzos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principal',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
