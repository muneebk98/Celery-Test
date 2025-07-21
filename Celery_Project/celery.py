# Celery_Project/celery.py

import os
from celery import Celery

# Set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Celery_Project.settings")

app = Celery("Celery_Project")

# Load Celery settings from Django's settings.py file
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks from all installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
