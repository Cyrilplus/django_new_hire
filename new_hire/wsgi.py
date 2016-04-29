"""
WSGI config for new_hire project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from app.sendmail import SendMail

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "new_hire.settings")

application = get_wsgi_application()

email = SendMail()
email.send2manager()
