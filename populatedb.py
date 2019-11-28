import csv
import os
from cgipf import settings


def populate() :
    with open(os.path.join(settings.BASE_DIR, 'gamesc2b2088.csv')) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = GamesList.objects.get_or_create(
                    title=row[0],
                    platform=row[1],
                    score=row[2],
                    genre=row[3],
                    editors_choice=row[4],
                    )


if __name__ == '__main__':
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cgipf.settings')
    django.setup()
    from glisting.models import GamesList
    populate()