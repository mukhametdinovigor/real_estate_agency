# Generated by Django 2.2.4 on 2021-05-18 20:25

from django.db import migrations


def transfer_flats(apps, schema):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        owner.flats.set(Flat.objects.filter(
            owner=owner.owner_name,
            owner_pure_phone=owner.owner_pure_phone,
        ))


class Migration(migrations.Migration):


    dependencies = [
        ('property', '0010_auto_20210515_2323'),
    ]

    operations = [
        migrations.RunPython(transfer_flats)
    ]