"""
WSGI config for task_manager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager_api.settings')

application = get_wsgi_application()

import os
import sys

# Add your project directory to the sys.path
sys.path.insert(0, '/home/BlessingEbele/task_manager_api')

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'task_manager_api.settings'

# Activate the virtual environment
activate_this = '/home/BlessingEbele/.virtualenvs/task_manager_env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import and initialize the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
