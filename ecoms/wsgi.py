import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNosie

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecoms.settings')

application = get_wsgi_application()
application = DjangoWhiteNosie(application)
