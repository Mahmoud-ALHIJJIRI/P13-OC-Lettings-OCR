from django.db import migrations

# 🚀 Forward migration function
def forwards(apps, schema_editor):
    """
    🔄 Migrate all Profile data from the old 'oc_lettings_site' app to the new 'profiles' app.
    """
    old_profile = apps.get_model('oc_lettings_site', 'Profile')
    profile = apps.get_model('profiles', 'Profile')

    for old in old_profile.objects.all():
        profile.objects.create(
            id=old.id,
            user_id=old.user_id,
            favorite_city=old.favorite_city,
        )

# 🔁 Backward migration function
def backwards(apps, schema_editor):
    """
    🚫 Delete all migrated Profile data from the 'profiles' app (rollback).
    """
    profile = apps.get_model('profiles', 'Profile')
    profile.objects.all().delete()

# 🛠️ Migration class
class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
