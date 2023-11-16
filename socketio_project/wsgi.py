"""
WSGI config for socketio_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import socketio
from socketio import Middleware,ASGIApp,WSGIApp
from socketio_app.views import sio
from django.core.wsgi import get_wsgi_application
import eventlet.wsgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socketio_project.settings')

app = get_wsgi_application()
application = Middleware(sio, app)
eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8000)), application)
