import os
import sys
import site

site.addsitedir('/var/www/pdf.voolks.com/ENV/lib/python2.7/site-packages')
sys.path.append('/var/www/pdf.voolks.com')
sys.path.append('/var/www/pdf.voolks.com/app')

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


