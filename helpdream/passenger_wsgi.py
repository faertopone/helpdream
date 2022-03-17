# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1581954/data/www/helpdream.ru/test_django')
sys.path.insert(1, '/var/www/u1581954/data/djangovenv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_django.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()