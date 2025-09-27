from django.db import migrations

# 🚀 Forward migration: Move data from 'oc_lettings_site' to 'lettings'
def forwards(apps, schema_editor):
    """
    🔄 Migrates Address and Letting data from the old 'oc_lettings_site' app
    to the new 'lettings' app.
    """
    # 🔍 Source models (old app)
    old_address = apps.get_model('oc_lettings_site', 'Address')
    old_letting = apps.get_model('oc_lettings_site', 'Letting')

    # 🎯 Target models (new app)
    address = apps.get_model('lettings', 'Address')
    letting = apps.get_model('lettings', 'Letting')

    # 📥 Migrate Address data
    for old in old_address.objects.all():
        address.objects.create(
            id=old.id,
            number=old.number,
            street=old.street,
            city=old.city,
            state=old.state,
            zip_code=getattr(old, 'zip_code', ''),
            country_iso_code=getattr(old, 'country_iso_code', ''),
        )

    # 📥 Migrate Letting data
    for old in old_letting.objects.all():
        letting.objects.create(
            id=old.id,
            title=old.title,
            address_id=old.address_id,
        )

# 🔁 Backward migration: Remove migrated data
def backwards(apps, schema_editor):
    """
    🗑️ Deletes all migrated Address and Letting data from the 'lettings' app.
    This rollback assumes data still exists in the original app.
    """
    # 🎯 Target models to clean up
    address = apps.get_model('lettings', 'Address')
    letting = apps.get_model('lettings', 'Letting')

    # ❌ Delete all records in new app
    address.objects.all().delete()
    letting.objects.all().delete()

# 🛠️ Migration definition
class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
