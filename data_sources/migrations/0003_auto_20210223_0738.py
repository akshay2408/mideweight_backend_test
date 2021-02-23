# Generated by Django 2.2.18 on 2021-02-23 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_sources', '0002_auto_20210223_0738'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='gatewaytag',
            name='gateway and label should be unique in GatewayTag.',
        ),
        migrations.RemoveConstraint(
            model_name='gatewaytag',
            name='gateway and hardware_name should be unique in GatewayTag.',
        ),
        migrations.AddConstraint(
            model_name='gatewaytag',
            constraint=models.UniqueConstraint(fields=('gateway_id', 'label'), name='gateway and label should be unique in GatewayTag.'),
        ),
        migrations.AddConstraint(
            model_name='gatewaytag',
            constraint=models.UniqueConstraint(fields=('gateway_id', 'hardware_name'), name='gateway and hardware_name should be unique in GatewayTag.'),
        ),
    ]