import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinalProject.settings')
django.setup()

from django.contrib.sites.models import Site

site, created = Site.objects.get_or_create(id=1, defaults={'domain': '127.0.0.1:8000', 'name': 'localhost'})
if created:
    print("Site created successfully.")
else:
    print("Site already exists.")
    site.domain = '127.0.0.1:8000'
    site.name = 'localhost'
    site.save()
    print("Site updated.")
