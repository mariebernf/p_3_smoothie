import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = get_wsgi_application()

application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), 'staticfiles'))
