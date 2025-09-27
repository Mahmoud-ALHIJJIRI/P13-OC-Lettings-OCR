"""import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
django.setup()


from oc_lettings_site.models import Address, Letting, Profile
from lettings.models import Address as NewAddress, Letting as NewLetting
from profiles.models import Profile as NewProfile


def migrate_addresses():
    for addr in Address.objects.all():
        NewAddress.objects.create(
            number=addr.number,
            street=addr.street,
            city=addr.city,
            state=addr.state,
            zip_code=addr.zip_code,
            country_iso_code=addr.country_iso_code,
        )


def migrate_lettings():
    for letting in Letting.objects.all():
        address = NewAddress.objects.get(street=letting.address.street)
        NewLetting.objects.create(
            title=letting.title,
            address=address
        )


def migrate_profiles():
    for profile in Profile.objects.all():
        NewProfile.objects.create(
            user=profile.user,
            favorite_city=profile.favorite_city
        )


if __name__ == '__main__':
    migrate_addresses()
    migrate_lettings()
    migrate_profiles()
    print("✅ Data migration complete.")
"""