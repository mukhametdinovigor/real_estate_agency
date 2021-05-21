# Generated by Django 2.2.4 on 2021-05-05 08:47

from django.db import migrations


def fill_new_building_field(apps, shema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.construction_year > 2014:
            flat.new_building = True
            flat.save()
        else:
            flat.new_building = False
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_building_field),
    ]