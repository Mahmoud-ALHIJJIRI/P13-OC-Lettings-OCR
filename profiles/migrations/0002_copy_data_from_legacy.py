from django.db import migrations


# 🚀 Forward migration function
def forwards(apps, schema_editor):
    """
    🔄 Migrate all Profile data from the old 'oc_lettings_site' app to the new 'profiles' app,
    safely skipping if old models aren't available (e.g., in a clean test run).
    """
    try:
        # 🔍 Source models (old app)
        # CRITICAL FIX: Wrap the historical model lookup in a try/except block.
        old_profile = apps.get_model('oc_lettings_site', 'Profile')

    except LookupError:
        # If the app/model state is missing (common in Pytest's clean test environment),
        # return immediately to prevent the test suite crash.
        print("Skipping Profile data migration: Old 'oc_lettings_site' models not found in this environment.")
        return

        # 🎯 Target model (new app) - This should always resolve.
    profile = apps.get_model('profiles', 'Profile')

    # 📥 Migrate Profile data (This only runs if the lookup above succeeded)
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
    # This lookup is safe as the 'profiles' app is actively installed.
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
